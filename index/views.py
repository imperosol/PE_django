from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout


def index(request):
    if request.user.is_authenticated:
        return render(request, 'index/index.html')
    else:
        context = {'next_page': request.GET.get('next', '')}
        # print(context['next_page'])
        return render(request, 'index/authenticate.html', context)


def login(request, next_page=''):
    context = {'next_page': next_page}
    return render(request, 'index/login.html', context)


def make_login(request, next_page='/'):
    username, password = request.POST['username'], request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        django_login(request, user)
    return redirect(next_page)
    # return render(request, 'index/login.html')


def create_account(request):
    return render(request, 'index/index.html')


def logout(request):
    if request.user.is_authenticated:
        django_logout(request)
    return redirect('/')

