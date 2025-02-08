from django.db import models
from django.utils import timezone

class Lead(models.Model):

    # Creating a choice field for the status of the lead
    STATUS_CHOICE = [
        ('pending', 'Pending'),
        ('verified', 'Verified'),
        ('analyzed', 'Analyzed'),
        ('email_generated', 'Email Generated'),
        ('email_sent', 'Email Sent'),
        ('completed', 'Completed')
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    website_url = models.URLField()
    website_title = models.CharField(max_length=200, blank=True, null=True)
    website_metadata = models.TextField(blank=True, null=True)
    summary_of_website = models.TextField(blank=True, null=True)
    ai_analysis = models.TextField(blank=True, null=True)
    personalized_email_text = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='pending')
    
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.email}"