from .models import Post, Category
from rest_framework.serializers import HyperlinkedModelSerializer, StringRelatedField
from django.contrib.auth.models import User


class PostSerializer(HyperlinkedModelSerializer):
    author = StringRelatedField(many=False)

    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'created_date', 'published_date', 'modified_date']


class CategorySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description', 'posts']