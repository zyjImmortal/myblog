from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from blog.apps.articles.models import Article


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()