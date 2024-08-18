# scraper.py
"""
Main scraping function for O Globo website.
This module contains the core logic for scraping articles from O Globo's Rio de Janeiro section.
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time
import random
from content_extractor import get_article_content
from data_processors import *
from utils import extract_date, get_coordinates, extract_important_metadata
from violence_classifier import ViolenceClassifier

def scrape_oglobo(days=365, start_page=1, max_pages=None):
    """
    Scrape articles from O Globo's Rio de Janeiro section.

    Args:
    days (int): Number of days to look back for articles.
    start_page (int): The page number to start scraping from.
    max_pages (int or None): Maximum number of pages to scrape. If None, scrape all available pages.

    Yields:
    dict: A dictionary containing data for each scraped article.
    """
    base_url = 'https://oglobo.globo.com/rio/'
    current_date = datetime.now()
    start_date = current_date - timedelta(days=days)
    
    # Initialize the violence classifier
    classifier = ViolenceClassifier()
    
    page = start_page
    
    while max_pages is None or page <= (start_page + max_pages - 1):
        print(f"Scraping page {page}...")
        response = requests.get(f"{base_url}?pagina={page}")
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('div', class_='feed-post')
        
        if not articles:
            print("No more articles found. Stopping.")
            break
        
        for article in articles:
            try:
                # Extract basic article information
                title_element = article.find('h2', class_='feed-post-title')
                title = title_element.text.strip() if title_element else article.find('a', class_='feed-post-link').text.strip()
                
                link_element = article.find('a', class_='feed-post-link')
                url = link_element['href'] if link_element else None
                
                # Extract and parse publication date
                date_element = article.find('span', class_='feed-post-datetime')
                if date_element:
                    pub_date_str = date_element.text.strip()
                    try:
                        pub_date = datetime.strptime(pub_date_str, '%d/%m/%Y %Hh%M')
                    except ValueError:
                        pub_date = current_date  # Use current date if parsing fails
                else:
                    pub_date = current_date
                
                if pub_date < start_date:
                    print(f"Reached articles older than {days} days. Stopping.")
                    return
                
                # Get full article content
                content = get_article_content(url) if url else ""
                
                # Predict violence likelihood
                violence_likelihood = classifier.predict_violence_likelihood(title + ' ' + content)
                
                # Skip articles with low violence likelihood
                if violence_likelihood < 0.3:
                    continue
                
                # Extract various data points from the content
                location = extract_location(content)
                important_metadata = extract_important_metadata(content)
                
                article_data = {
                    'Newspaper': 'O Globo',
                    'Crime Date': extract_date(content) or pub_date,
                    'Coordinates': get_coordinates(location),
                    'Location': location,
                    'Description': title,
                    'Police Involvement': extract_police_involvement(content),
                    'Gang/Organized Group Involvement': extract_gang_involvement(content),
                    'Number of Victims': extract_victims(content),
                    'Gender of Victims': extract_gender(content),
                    'Level of Violence': determine_violence_level(content),
                    'Type of Violence': determine_violence_type(content),
                    'Journalist': extract_journalist(content),
                    'Article Date': pub_date,
                    'Keywords': 'violência',
                    'Notes': '',
                    'Link': url,
                    'Content': content,
                    'Important Metadata': important_metadata,
                    'Violence Likelihood': f"{violence_likelihood:.2f}",
                    'Likely Violent Event': "High" if violence_likelihood > 0.7 else "Medium" if violence_likelihood > 0.4 else "Low"
                }
                
                yield article_data
                
            except Exception as e:
                print(f"Error processing article: {e}")
                continue
        
        page += 1
        time.sleep(random.uniform(5, 10))  # Be polite to the server
    
    print(f"Finished scraping articles from {page-1} pages.")