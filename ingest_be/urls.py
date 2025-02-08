from django.urls import path
from .views import LeadListCreateView, LeadRetrieveUpdateView, LeadAnalyzeView, LeadGenerateEmailView, LeadSendEmailView, LeadScraperView, BulkLeadListCreateView

app_name = 'ingest_be'

urlpatterns = [
    # Create and View Leads [method: GET, POST]
    path('leads/', LeadListCreateView.as_view(), name='lead-list-create'),

    # Bulk Create Leads [method: POST]
    path('leads/bulk/', BulkLeadListCreateView.as_view(), name='bulk-lead-list-create'),

    # Retrieve and Update Lead [method: GET, PUT]
    path('leads/<int:pk>/', LeadRetrieveUpdateView.as_view(), name='lead-retrieve-update'),

    # Scrape Lead [method: PUT]
    path('leads/<int:pk>/scrape/', LeadScraperView.as_view(), name='lead-scraper'),

    # Analyze Lead [method: PUT]
    path('leads/<int:pk>/analyze/', LeadAnalyzeView.as_view(), name='lead-analyze'),

    # Generate Email [method: PUT]
    path('leads/<int:pk>/generate_email/', LeadGenerateEmailView.as_view(), name='lead-generate-email'),

    # Send Email [method: PUT]
    path('leads/<int:pk>/send_email/', LeadSendEmailView.as_view(), name='lead-send-email'),
]
