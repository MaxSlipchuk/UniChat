from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.http.response import HttpResponseNotFound, HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from users.forms import LoginUserForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.

# клас для відображення сторінки
# class UsersPage(View):
#     # для обробки get
#     def get(self, request):
#         form = LoginUserForm()
#         return render(request, 'users/users.html', context={'form': form})

#     # для обробки post
#     def post(self, request):
#         form = LoginUserForm()
#         return render(request, 'users/users.html', context={'form': form})


def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username = cd['username'], password = cd['password'])
            # перевірка чи користувач є і чи він не забанений
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('main'))
    else:
        form = LoginUserForm()
    return render(request, 'users/users.html', context={'form': form})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))




# class Account(View):
#     # для обробки get
#     def get(self, request):
#         return render(request, 'account/account.html')
    
#     # для обробки post
#     def post(self, request):
#         print("форма відпрвлена")
#         return render(request, 'account/account.html')

    

    
