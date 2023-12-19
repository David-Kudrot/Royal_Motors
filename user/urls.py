from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserProfileView, UpdateUser, PasswordChange
from . import views

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('update_profile/<int:pk>/', UpdateUser.as_view(), name='update_profile'),
    path('logout/', views.log_out, name='logout'),
    path('buy/<int:id>/', views.buy_car, name='buy'),
    path('change_password/', PasswordChange.as_view(), name='change_password'),
]
