from django.urls import path

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from anime import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'anime', views.AnimeViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'comment', views.CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
