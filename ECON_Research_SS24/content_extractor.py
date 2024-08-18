# content_extractor.py
"""
Functions for extracting content from article URLs.
This module handles the retrieval and parsing of full article content.
"""

import requests
from bs4 import BeautifulSoup
import re
import time

def get_article_content(url, max_retries=3):
    """
    Retrieve and extract the main content of an article from its URL.
    
    Args:
    url (str): The URL of the article to scrape.
    max_retries (int): Maximum number of retry attempts for failed requests.
    
    Returns:
    str: The extracted article content or an empty string if extraction fails.
    """
    if not url:
        return ""
    
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Try different selectors for article content
            content_selectors = [
                'div.article__content',
                'div.materia-conteudo',
                'div.content-text',
                'article',
                'div.corpo'
            ]
            
            for selector in content_selectors:
                content = soup.select_one(selector)
                if content:
                    # Remove unwanted elements
                    for unwanted in content.select('script, style, iframe, .advertisement'):
                        unwanted.decompose()
                    
                    # Extract text and clean it up
                    text = ' '.join(p.get_text(strip=True) for p in content.find_all('p'))
                    text = re.sub(r'\s+', ' ', text).strip()
                    
                    if text:
                        return text
            
            # If no content found with selectors, try getting all paragraph text
            all_paragraphs = soup.find_all('p')
            if all_paragraphs:
                text = ' '.join(p.get_text(strip=True) for p in all_paragraphs)
                return re.sub(r'\s+', ' ', text).strip()
            
            print(f"No content found for URL: {url}")
            return ""
        
        except requests.RequestException as e:
            if attempt < max_retries - 1:
                print(f"Error fetching article content: {e}. Retrying...")
                time.sleep(2)  # Wait before retrying
            else:
                print(f"Failed to fetch article content after {max_retries} attempts: {e}")
                return ""

    return ""