from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Biography, Endorse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView


def home(request):
    """
    Handle the request for the home page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered home page.
    """
    return render(request, 'home.html')


@login_required
def biography_view(request):
    """
    Handle the request for the candidate's biography page.

    This view requires the user to be logged in.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered biography page.
    """
    biographies = Biography.objects.all()
    return render(request, 'candidate/biography.html', {'biographies': biographies})


@login_required
def endorse_view(request):
    """
    Handle the request for the candidate's endorsement page.

    This view requires the user to be logged in.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered endorsement page.
    """
    endorsements = Endorse.objects.all()
    return render(request, 'candidate/endorse.html',  {'endorsements': endorsements})


def register(request):
    """
    Handle user registration.

    If the request method is POST, validate the form and save the new user.
    Log the user in and redirect to the home page upon successful registration.
    If the request method is GET, display an empty registration form.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered registration page with the form.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('candidate:home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


class CustomLoginView(LoginView):
    """
    Custom login view that uses a specific template.

    Attributes:
        template_name (str): The name of the template to use for the login page.
    """
    template_name = 'login.html'


class CustomLogoutView(LogoutView):
    """
    Custom logout view that redirects to a specific page after logout.

    Attributes:
        next_page (str): The name of the page to redirect to after logout.
    """
    next_page = 'home'


class HomeView(TemplateView):
    """
    View for rendering the home page.

    Attributes:
        template_name (str): The name of the template to use for the home page.
    """
    template_name = 'home.html'
