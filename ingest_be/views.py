from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
import pandas as pd
from .models import Lead
from .serializers import LeadSerializer
import os
import smtplib
from email.message import EmailMessage
from .services.email_generator import EmailGenerator
from .services.webscraper import WebsiteScraper
from .services.ai_analyzer import AIAnalyzer

# Creating a class to list and create leads
# This class will handle the GET and POST requests for the leads
class LeadListCreateView(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer


# Creating a class to bulk create leads
# This class will handle the POST request for bulk lead creation
class BulkLeadListCreateView(generics.CreateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = LeadSerializer

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        if not file:
            return Response({'error': 'No file uploaded'}, status=status.HTTP_400_BAD_REQUEST)

        # Read the CSV file and create Lead objects
        df = pd.read_csv(file)
        leads = [Lead(name=row['name'], email=row['email'], website_url=row['website_url']) for _, row in df.iterrows()]

        # Bulk create the Lead objects
        Lead.objects.bulk_create(leads)
        # Return a success response
        return Response({'message': 'Leads uploaded successfully'}, status=status.HTTP_201_CREATED)


# Creating a class to retrieve and update leads
# This class will handle the GET and PUT requests for the leads
class LeadRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer


# Creating a class to scrape the website content of a lead
# This class will handle the PUT request to scrape the website content
class LeadScraperView(generics.UpdateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

    def perform_update(self, serializer):
        lead = self.get_object()

        # Scrape the website content
        webscraper = WebsiteScraper()
        website_content = webscraper.retrieve_content(lead.website_url)

        # Update the lead object with the scraped content
        lead.website_title = website_content['title']
        lead.website_metadata = website_content['meta_desc']
        lead.summary_of_website = website_content['content']
        lead.status = 'verified'
        lead.save()

        # Save the updated lead object
        serializer.save(
            website_title=lead.website_title,
            website_metadata=lead.website_metadata,
            summary_of_website=lead.summary_of_website, 
            status=lead.status, 
            partial=True
        )


# Creating a class to analyze the website content of a lead
# This class will handle the PUT request to analyze the website content
class LeadAnalyzeView(generics.UpdateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

    def perform_update(self, serializer):
        lead = self.get_object()

        # Analyze the website content
        analysis = AIAnalyzer()
        website_content = analysis.analyze_website(lead.website_title, lead.website_metadata, lead.summary_of_website)

        # Update the lead object with the analyzed content
        lead.ai_analysis = website_content
        lead.status = 'analyzed'
        lead.save()
        # Save the updated lead object
        serializer.save(
            ai_analysis=lead.ai_analysis,
            status=lead.status,
            partial=True
        )


# Creating a class to generate a personalized email for a lead
# This class will handle the PUT request to generate a personalized email
class LeadGenerateEmailView(generics.UpdateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

    def perform_update(self, serializer):
        lead = self.get_object()
        
        # Generate a personalized email for the lead
        email_generator = EmailGenerator()
        response = email_generator.generate_personalized_email(lead.name, lead.website_title, lead.website_metadata, lead.summary_of_website)

        # Update the lead object with the personalized email text
        lead.personalized_email_text = response
        lead.status = 'email_generated'
        lead.save()
        # Save the updated lead object
        serializer.save(
            personalized_email_text=lead.personalized_email_text,
            status=lead.status,
            partial=True
        )


# Creating a class to send an email to a lead
# This class will handle the PUT request to send an email to a lead
class LeadSendEmailView(generics.UpdateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

    # Method to send an email to the lead
    def perform_update(self, serializer):
        lead = self.get_object()
        email_msg = EmailMessage()
        email_msg.set_content(lead.personalized_email_text)
        email_msg['Subject'] = f"Personalized Outreach to {lead.name}"
        email_msg['From'] = os.getenv("EMAIL_SENDER")
        email_msg['To'] = lead.email

        with smtplib.SMTP(os.getenv("SMTP_SERVER"), int(os.getenv("SMTP_PORT"))) as server:
            server.starttls()
            server.login(os.getenv("EMAIL_SENDER"), os.getenv("EMAIL_PASSWORD"))
            server.send_message(email_msg)

        lead.status = 'email_sent'
        lead.save()
        # Save the updated lead object
        serializer.save(
            status=lead.status,
            partial=True
        )