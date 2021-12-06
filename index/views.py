from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.models import User
from django.core.validators import validate_email, ValidationError


def index(request):
    if request.user.is_authenticated:
        return render(request, 'index/index.html')
    context = {'next_page': request.GET.get('next', '')}
    return render(request, 'index/authenticate.html', context)


def login(request, next_page = ''):
    context = {'next_page': next_page}
    return render(request, 'index/login.html', context)


def make_login(request, next_page = '/'):
    username, password = request.POST['username'], request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is None:
        context = {
            'next_page': next_page,
            'error': 'Connexion impossible : utilisateur inexistant ou mot de passe erroné'
        }
        return render(request, 'index/login.html', context)
    django_login(request, user)
    return redirect(next_page)


def sign_up(request, next_page = ''):
    context = {'next_page': next_page}
    return render(request, 'index/sign_up.html', context)


def is_valid_email(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False


def create_account(request, next_page = '/'):
    context = {
        'next_page': next_page,
        'error': [],
        'error_signal': []
    }
    if User.objects.filter(username=request.POST['username']).exists():
        context['error'].append("Un utilisateur se nomme déjà ainsi")
        context['error_signal'].append('username')
    if request.POST['password'] != request.POST['password-confirm']:
        context['error'].append("Le mot de passe et la confirmation ne correspondent pas")
        context['error_signal'] += ['password', 'password-confirm']
    if not is_valid_email(request.POST['email']):
        context['error'].append("L'adresse email est invalide")
        context['error_signal'].append('email')
    if len(context['error']) > 0:
        return render(request, 'index/sign_up.html', context)
    user = request.POST
    user = User.objects.create(username=user['username'], password=user['password'],
                               first_name=user['first-name'], last_name=user['last-name'], email=user['email'])
    django_login(request, user)
    return redirect(next_page)


def logout(request):
    if request.user.is_authenticated:
        django_logout(request)
    return redirect('/')
