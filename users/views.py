from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.http.response import HttpResponseNotFound, HttpResponse, HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from users.forms import LoginUserForm, RegisterUserForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.

def login_user(request):

    login_form = LoginUserForm()
    register_form = RegisterUserForm()

    if request.method == 'POST':
        print(f'\n method post')
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # перевірка, що це fetch
            print('ajax request')
            # if 'register_submit' in request.POST:
            print('register submit button')
            register_form = RegisterUserForm(request.POST)
            login_form    = LoginUserForm()
            if register_form.is_valid():
                print('if valid register')
                user = register_form.save()
                print(user)
                # login(request, user)
                # return HttpResponseRedirect(reverse('main'))
            else:
                print('register form not valid')
                print(register_form.errors)
                return JsonResponse({
                    'success': 'false',
                    'errors': register_form.errors
                })
        else:
            if 'login_submit' in request.POST:
                login_form    = LoginUserForm(request.POST)
                register_form = RegisterUserForm()
                print('login submit button')

                if login_form.is_valid():
                    print('if valid login')
                    cd = login_form.cleaned_data
                    print(cd)
                    user = authenticate(request, username = cd['username'], password = cd['password'])
                    print(user)
                    # перевірка чи користувач є і чи він не забанений
                    if user and user.is_active:
                        login(request, user)
                        print('форма логін')
                        return HttpResponseRedirect(reverse('main'))


            print('not ajax request')
            return HttpResponseNotFound('<h2>Page not found</h2>')
    else:
        login_form = LoginUserForm()
        register_form = RegisterUserForm()
    return render(request, 'users/users.html', context={
                                                        'login_form': login_form,
                                                        'register_form': register_form
                                                        })

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))

    
