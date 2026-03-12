from django.shortcuts import render
from .models import NewsArticle
from .utils import fetch_financial_news

def index(request):
    fetch_financial_news() # Triggers the pipeline on page load
    
    # 1. Base Query: Get everything for the chart counts
    all_articles = NewsArticle.objects.all()
    positive_count = all_articles.filter(sentiment_label='Positive').count()
    negative_count = all_articles.filter(sentiment_label='Negative').count()
    neutral_count = all_articles.filter(sentiment_label='Neutral').count()
    
    # 2. Sliced Query: Get ONLY the top 50 for the table display
    recent_articles = all_articles.order_by('-published_at')[:50]
    
    context = {
        'articles': recent_articles,
        'positive_count': positive_count,
        'negative_count': negative_count,
        'neutral_count': neutral_count,
    }
    
    return render(request, 'dashboard/index.html', context)