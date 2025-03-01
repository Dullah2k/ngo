from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

app_name = "user_auth"
urlpatterns = [
  path('login/', auth_views.LoginView.as_view(), name="login"),
  path('logout/', auth_views.LogoutView.as_view(), name="logout"),
  path('org_register/', views.organization_registration, name="organization_registration"),
]