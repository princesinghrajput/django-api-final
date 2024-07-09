from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet, CommentViewSet, CustomAuthToken

router = DefaultRouter()
router.register(r'blogs', BlogViewSet)
router.register(r'blogs/(?P<blog_pk>[^/.]+)/comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', CustomAuthToken.as_view()),
]
