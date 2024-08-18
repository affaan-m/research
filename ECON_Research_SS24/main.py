# main.py
"""
Main execution script for the O Globo violence scraper.
This script coordinates the scraping process, data saving, and output.
"""

import csv
import pandas as pd
from scraper import scrape_oglobo
from datetime import datetime

def main():
    scraped_data = []
    csv_filename = 'violence_data.csv'
    start_page = 200  # Set the starting page
    max_pages = 5  # Set to None to scrape all available pages
    days = 3650  # Scrape articles from the last 10 years

    # Define the fields for our CSV file
    fieldnames = ['Newspaper', 'Crime Date', 'Coordinates', 'Location', 'Description', 
                  'Police Involvement', 'Gang/Organized Group Involvement', 'Number of Victims', 
                  'Gender of Victims', 'Level of Violence', 'Type of Violence', 'Journalist', 
                  'Article Date', 'Keywords', 'Notes', 'Link', 'Content', 'Important Metadata',
                  'Violence Likelihood', 'Likely Violent Event']

    try:
        # Create and write headers to the CSV file
        with open(csv_filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

        # Scrape articles and write them to the CSV file
        for article in scrape_oglobo(days=days, start_page=start_page, max_pages=max_pages):
            scraped_data.append(article)
            
            # Write each article to CSV immediately
            with open(csv_filename, 'a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writerow(article)
            
            print(f"Article scraped and saved. Total articles: {len(scraped_data)}")
            
    except KeyboardInterrupt:
        print("\nScript terminated by user. Saving collected data...")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
    finally:
        print(f"\nTotal articles scraped and saved: {len(scraped_data)}")
        
        if scraped_data:
            # Display a summary of the scraped data
            for i, article in enumerate(scraped_data[:10], 1):  # Show first 10 articles
                print(f"\n{i}. {article['Description']}")
                print(f"   Date: {article['Article Date']}")
                print(f"   URL: {article['Link']}")
                print(f"   Location: {article['Location']}")
                print(f"   Violence Likelihood: {article['Violence Likelihood']}")
                print(f"   Likely Violent Event: {article['Likely Violent Event']}")
            
            if len(scraped_data) > 10:
                print("\n... (more articles not shown)")
            
            print(f"\nData saved to '{csv_filename}'")

            # Create a DataFrame and save to CSV
            df = pd.DataFrame(scraped_data)
            df.to_csv('violence_data_df.csv', index=False)
            print("Data also saved as DataFrame to 'violence_data_df.csv'")
        else:
            print("No data was collected before the script was terminated.")

if __name__ == "__main__":
    main()