from django.urls import path
from .views import RegisterView, LoginView, UserProfileView, DeleteAccountView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('login/', LoginView.as_view(), name='auth_login'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('delete-account/', DeleteAccountView.as_view(), name='delete_account'),
]
