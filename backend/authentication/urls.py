from django.urls import path
from authentication.views import LoginView, RegisterView, UpdateView, ChangePassword, logout_view

app_name = 'authentication'

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name="register"),
    path('update/', UpdateView.as_view(), name='update'),
    path('change_password/<int:pk>/', ChangePassword.as_view(), name='change-password'),
    path('logout/', logout_view, name="logout"),
]
