# utils.py
"""
Utility functions for the O Globo violence scraper.
This module contains helper functions for date extraction and geolocation.
"""

from datetime import datetime
from geopy.geocoders import Nominatim
import re

def extract_date(text):
    """
    Extract a date from the given text.
    
    Args:
    text (str): The text to search for a date.
    
    Returns:
    datetime or None: The extracted date if found, None otherwise.
    """
    date_match = re.search(r'\d{1,2}/\d{1,2}/\d{4}', text)
    if date_match:
        return datetime.strptime(date_match.group(), '%d/%m/%Y')
    return None

def get_coordinates(location):
    """
    Get the geographic coordinates for a given location.
    
    Args:
    location (str): The name of the location to geocode.
    
    Returns:
    str: A string containing latitude and longitude, or "N/A" if geocoding fails.
    """
    geolocator = Nominatim(user_agent="violence_scraper")
    try:
        # Attempt to geocode the location
        location_info = geolocator.geocode(location)
        if location_info:
            return f"{location_info.latitude}, {location_info.longitude}"
    except Exception as e:
        # Log the error if geocoding fails
        print(f"Error in geocoding {location}: {e}")
    return "N/A"

# You can add more utility functions here as needed, for example:

def clean_text(text):
    """
    Clean and normalize text.
    
    Args:
    text (str): The text to clean.
    
    Returns:
    str: The cleaned text.
    """
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    # You can add more cleaning steps here, such as removing special characters,
    # normalizing accents, etc.
    return text

def format_date(date):
    """
    Format a date object to a standard string format.
    
    Args:
    date (datetime): The date to format.
    
    Returns:
    str: The formatted date string.
    """
    if date:
        return date.strftime('%Y-%m-%d')
    return "Unknown"

# Add any other utility functions that might be useful across the project

def extract_important_metadata(content):
    """
    Extract important metadata from the article content.
    This function can be customized based on what you consider important metadata.

    Args:
    content (str): The full text content of the article.

    Returns:
    str: A string containing important metadata extracted from the content.
    """
    metadata = []

    # Extract the first sentence (often a summary)
    first_sentence = content.split('.')[0] + '.'
    metadata.append(f"Summary: {first_sentence}")

    # Extract any mentioned dates
    dates = re.findall(r'\d{1,2}/\d{1,2}/\d{4}', content)
    if dates:
        metadata.append(f"Mentioned dates: {', '.join(dates)}")

    # Extract any mentioned names (this is a simple example and might need refinement)
    names = re.findall(r'\b[A-Z][a-z]+ [A-Z][a-z]+\b', content)
    if names:
        metadata.append(f"Mentioned names: {', '.join(set(names[:5]))}")  # Limit to first 5 unique names

    # You can add more metadata extraction here

    return '; '.join(metadata)