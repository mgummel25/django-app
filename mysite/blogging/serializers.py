from django.contrib.auth.models import User, Group

from .models import Post, Category
from rest_framework.serializers import HyperlinkedModelSerializer, StringRelatedField


class PostSerializer(HyperlinkedModelSerializer):
    author = StringRelatedField(many=False)

    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'created_date', 'published_date', 'modified_date']


class CategorySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description', 'posts']


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']