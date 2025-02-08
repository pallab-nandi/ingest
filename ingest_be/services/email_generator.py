from anthropic import Anthropic
import os
from dotenv import load_dotenv

load_dotenv()

# Creating a class to generate personalized email content using Anthropic AI API
class EmailGenerator:
    def __init__(self):
        self.client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

    def generate_personalized_email(self, lead_name, website_title, website_metadata, website_summary):
        try:
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20240620",
                max_tokens=500,

                # Creating a message prompt to generate personalized email content
                messages=[
                    {
                        "role": "user", 
                        "content": f"""Generate a personalized, professional email outreach message.

                                    Lead Name: {lead_name}
                                    Website Title: {website_title}
                                    Website Metadata: {website_metadata}
                                    Website Summary: {website_summary}

                                    Requirements:
                                    - Keep it concise (3-4 paragraphs)
                                    - Sound professional and engaging
                                    - Reference specific details from the website summary
                                    - Include a clear call-to-action"""
                    }
                ]
            )
            return response.content[0].text
        except Exception as e:
            return f"Email Generation Error: {str(e)}"