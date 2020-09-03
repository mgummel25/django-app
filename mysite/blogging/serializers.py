from .models import Post, Category
from rest_framework.serializers import HyperlinkedModelSerializer


class PostSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
        ]


class CategorySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description', 'posts']