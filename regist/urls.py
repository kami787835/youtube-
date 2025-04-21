from django.urls import path
from .views import CustomUserRegisterView, UserLoginView

urlpatterns = [
    path('register/', CustomUserRegisterView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
]