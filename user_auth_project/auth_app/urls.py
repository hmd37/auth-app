from django.urls import path
from .views import Home, RegisterView, oauth_view, home


urlpatterns = [
    path('api/', Home.as_view(), name='api'),
    path('register/', RegisterView.as_view(), name='register'),
    path('oauth-test/', oauth_view, name='ouath-test'),
    path('', home, name='home')
]
