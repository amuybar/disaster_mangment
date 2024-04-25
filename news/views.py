from django.shortcuts import render
from .models import NewsArticle

def news(request):
    articles = NewsArticle.objects.all()
    return render(request, 'news.html', {'articles': articles})
