from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

app_name = "organization"
urlpatterns = [
  path('dashboard/', views.dashboard, name="dashboard"),
]