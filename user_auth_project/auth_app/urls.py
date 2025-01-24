from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import RegisterView, GoogleLoginView, UserProfileView, home, oauth_view


urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('api/google-login/', GoogleLoginView.as_view(), name='google_login'),
    
    path('api/profile/', UserProfileView.as_view(), name='user_profile'),

    path('oauth-test/', oauth_view, name='ouath-test'),
    path('', home, name='home'),
    path('social-auth/', include('social_django.urls', namespace='social')),
]
