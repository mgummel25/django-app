from django.urls import path, include
from .views import list_view, detail_view, PostViewSet, CategoryViewSet, UserViewSet, GroupViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'posts', PostViewSet)
router.register(r'users', UserViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('blog/', list_view, name="blog_index"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail")
]
