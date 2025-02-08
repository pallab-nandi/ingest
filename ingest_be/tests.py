from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Lead

# Lead creation API test
class LeadAPITestCase(APITestCase):
    def test_create_lead_api(self):
        data = {"name": "API Lead", "email": "api@example.com", "website_url": "https://example.com"}
        response = self.client.post("/api/v1/leads/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "API Lead")

# Model test
class LeadModelTest(TestCase):
    def test_create_lead(self):
        lead = Lead.objects.create(
            name="Test Lead",
            email="test@example.com",
            website_url="https://example.com"
        )
        self.assertEqual(lead.status, "pending")