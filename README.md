# Stock Market Analysis by Scraping Data from Reddit

This Jupyter Notebook provides an analysis of the relationship between sentiment trends and stock market performance for major tech companies.

## Table of Contents
- [Features](#features)
- [How to Use](#how-to-use)
- [Data Sources](#data-sources)
- [Requirements](#requirements)
- [Outputs](#outputs)

## Features

1. **Data Preprocessing**:
   - Clean and organize datasets.
   - Handle company mentions in Reddit data.

2. **Sentiment Analysis**:
   - Analyze Reddit posts for sentiment using Hugging Face's transformers.

3. **Stock Data Processing**:
   - Fetch historical stock data using the Yahoo Finance API.
   - Calculate financial metrics like Moving Averages (MA) and Returns.

4. **Data Visualization**:
   - Generate figures showing trends in sentiment and stock prices.
   - Correlation heatmaps to identify relationships between sentiment and financial performance.
   - Scatter plots and regression lines for sentiment vs. returns.

5. **Modeling**:
   - Apply linear regression to model the impact of sentiment on stock performance.

## How to Use

1. Clone the repository and navigate to the directory:
```bash
   git clone <repository-url>
   cd <repository-directory>
```

2. Create a virtual environment in the directory:
```python
python -m venv .venv
```

3. Activate the virtual environment:
- On Windows:
```bash
   .venv\Scripts\activate
```
- On Mac OS/Linux:
```bash
source .venv/bin/activate
```

4. Install required dependencies:
```python
    pip install -r requirements.txt
```

5. Get the Reddit API credentials from this [Link](https://old.reddit.com/prefs/apps)
<br>
6. Create an app and paste the credentials into **.env** file (**env.example** file created for the structure):<br>
```
CLIENT_ID = your_reddit_client_id
CLIENT_SECRET = your_reddit_client_secret
USER_AGENT = your_app_user_agent
```
<br>

7. Run the **`scrap.py`** file to scrape data from the Reddit website. This will generate a CSV file (`tech_threads_last_year.csv`) in the `data/` directory:
```python
    python scrap.py
```

8. Run the notebook in Jupyter or your preferred IDE to view the results

## Data Sources
- **Reddit Data**: Posts about tech companies from the past year.
- **Stock Data**: Historical stock prices fetched using Yahoo Finance.

## Requirements
- Python 3.8+
- IDE (VSCode for example)
- Jupyter Notebook

### Libraries:
- praw
- pandas
- python-dotenv
- matplotlib
- yfinance
- transformers
- tensorflow
- seaborn
- tf-keras
- scikit-learn

## Outputs
- **Trend Analysis**: Plots combining sentiment data and stock performance.
- **Correlation Heatmaps**: Visualizations showing relationships between sentiment and stock metrics.
- **Regression Models**: Insights into how sentiment influences stock returns.
