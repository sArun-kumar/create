
from rest_framework import viewsets

from .models import  Article
from .serializers import ArticleSerializers

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('title')
    serializer_class =  ArticleSerializers
