from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView

from .models import Article
from .serializers import ArticleInfoSerializer

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()

class ArticleInfoViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleInfoSerializer