from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import views
from .views import CustomLoginView, CustomLogoutView, register
from .views import HomeView


app_name = 'candidate'
urlpatterns = [
    # Home page
    path('', HomeView.as_view(), name='home'),
    # Biography page, requires login
    path('biography/', login_required(views.biography_view), name='biography'),
    # Endorse page, requires login
    path('endorse/', login_required(views.endorse_view), name='endorse'),
    # Register page
    path('register/', register, name='register'),
    # login page.
    path('login/', CustomLoginView.as_view(), name='login'),
    # logout page.
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
