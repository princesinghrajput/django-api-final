from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog_app.views import BlogViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'blogs', BlogViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
