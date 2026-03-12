import os
import requests
from textblob import TextBlob
from dotenv import load_dotenv
from .models import NewsArticle
from django.utils.dateparse import parse_datetime

# Load the hidden variables from the .env file
load_dotenv()

# Securely fetch the API key
API_KEY = os.getenv('NEWS_API_KEY')

def fetch_financial_news(query="Thomson Reuters"):
    url = f'https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey={API_KEY}'
    response = requests.get(url).json()
    
    if response.get('articles'):
        for art in response['articles'][:15]: # Process 15 articles
            text = (art['title'] or "") + " " + (art['description'] or "")
            sentiment = TextBlob(text).sentiment.polarity
            
            label = "Neutral"
            if sentiment > 0.1: label = "Positive"
            elif sentiment < -0.1: label = "Negative"

            # Save to Database (Avoid duplicates)
            NewsArticle.objects.update_or_create(
                url=art['url'],
                defaults={
                    'title': art['title'],
                    'published_at': parse_datetime(art['publishedAt']),
                    'sentiment_score': round(sentiment, 2),
                    'sentiment_label': label,
                    'summary': art['description']
                }
            )