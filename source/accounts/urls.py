from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from accounts.views import RegisterView, UserDetailView, UserUpdateView, UserPasswordChangeView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', RegisterView.as_view(), name='registration'),
    path('<int:pk>/', UserDetailView.as_view(), name='detail'),
    path('profile/', UserUpdateView.as_view(), name='update_profile'),
    path('change_password/', UserPasswordChangeView.as_view(), name='change_password'),
]