import praw
import pandas as pd
import time
import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Check if environment variables are set
if not all([os.getenv('CLIENT_ID'), os.getenv('CLIENT_SECRET'), os.getenv('USER_AGENT')]):
    logging.error("Reddit API credentials are not set in environment variables.")
    exit(1)

# Reddit API credentials from environment variables
reddit = praw.Reddit(
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    user_agent=os.getenv('USER_AGENT')
)

# List of stock-related subreddits
subreddits = ["stocks", "investing", "wallstreetbets"]

# List of major tech companies
tech_companies = ["Apple", "Google", "Microsoft", "Amazon", "Meta"]

# Initialize an empty list to store data
all_data = []

# Function to get data for each company and subreddit
for company in tech_companies:
    for sub in subreddits:
        logging.info(f"Fetching data for company: {company} in subreddit: {sub}")
        # Fetch threads for each month in the last year
        for i in range(12):
            logging.info(f"  Fetching data for month: {i+1}")
            try:
                # Try to fetch data for the specific month
                subreddit = reddit.subreddit(sub)
                threads = subreddit.search(company, sort='new', time_filter='month')
                
                for thread in threads:
                    thread.comments.replace_more(limit=0)
                    comments = " ".join([comment.body for comment in thread.comments.list()])
                    all_data.append({
                        'date_utc': pd.to_datetime(thread.created_utc, unit='s'),
                        'timestamp': thread.created_utc,
                        'title': thread.title,
                        'text': thread.selftext,
                        'subreddit': sub,
                        'comments': comments,
                        'url': thread.url
                    })
                
                # Pause to avoid rate limits
                time.sleep(1)  # Adjust this delay depending on API rate limits
            except Exception as e:
                logging.error(f"Error fetching data for {company} in {sub} for month {i+1}: {e}")

# Convert the list to a DataFrame
logging.info("Converting data to DataFrame")
combined_data = pd.DataFrame(all_data)

# Sort the data by company
logging.info("Sorting data by company")
sorted_data = combined_data.sort_values(by='date_utc')

# Create the data directory if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Save the sorted data to a CSV file
logging.info("Saving data to CSV file")
sorted_data.to_csv('data/tech_threads_year_sorted.csv', index=False)

# Confirmation message
logging.info("Data saved successfully as 'tech_threads_year_sorted.csv'")