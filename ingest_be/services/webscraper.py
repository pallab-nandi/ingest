import requests
from bs4 import BeautifulSoup
import logging

# Class to scrape website content
class WebsiteScraper:
    @staticmethod
    def retrieve_content(url):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract title and paragraphs
            title = soup.title.string if soup.title else "No Title"
            meta_desc = soup.find("meta", attrs={"name": "description"})
            meta_desc_content = meta_desc["content"] if meta_desc else 'No meta description' # Extract meta description content
            paragraphs = [p.get_text() for p in soup.find_all("p")[:3]]  # Extract first 3 paragraphs

            if not paragraphs:
                headings = [h.get_text() for h in soup.find_all(["h1", "h2", "h3"])[:3]]
                content_summary = " | ".join(headings) if headings else 'No content found'
            else:
                content_summary = " ".join(paragraphs)

            
            return {
                'title': title,
                'meta_desc': meta_desc_content,
                'content': content_summary
            }
        except requests.RequestException as e:
            logging.error(f"Error scraping {url}: {e}")
            return {
                'title': 'Error',
                'content': 'Could not retrieve website content'
            }