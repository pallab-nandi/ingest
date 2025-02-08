import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

# Creating a class to analyze the website content using Anthropic AI API
class AIAnalyzer:
    def __init__(self):
        self.client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

    def analyze_website(self, website_title, website_metadata, website_content):
        try:
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20240620",
                max_tokens=300,

                # Creating a message prompt to analyze the website content
                messages=[
                    {
                        "role": "user", 
                        "content": f"Provide a concise summary of this website's content and purpose:\n\n Website Title: {website_title} \n Meta Description: {website_metadata} \n Content: {website_content}"
                    }
                ]
            )
            return response.content[0].text
        except Exception as e:
            return f"AI Analysis Error: {str(e)}"