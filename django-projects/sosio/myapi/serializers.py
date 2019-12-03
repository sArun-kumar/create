from rest_framework import serializers
from .models import Article

class ArticleSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('title' , 'discription')

