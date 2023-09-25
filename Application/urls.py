from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('upload/', views.upload, name='upload'),
    path('upload_success/', views.upload_success, name='upload_success'),
    # Other URL patterns
]
