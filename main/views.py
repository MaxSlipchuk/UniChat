from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseNotFound, HttpResponse, HttpResponseRedirect
from users.forms import LoginUserForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


# Create your views here.

# class MainPage(LoginRequiredMixin, TemplateView):
#     template_name = 'main/main.html'



def main(request):
    if request.method == 'POST':
        if 'login_submit' in request.POST:
            login_form = LoginUserForm(request.POST)
            # register_form = RegisterUserForm(request.POST)
            if login_form.is_valid():
                print('if valid login')
                cd = login_form.cleaned_data
                user = authenticate(request, username = cd['username'], password = cd['password'])
                # перевірка чи користувач є і чи він не забанений
                if user and user.is_active:
                    login(request, user)
                    print('форма логін')
                    return HttpResponseRedirect(reverse('main'))
        # elif 'register_submit' in request.POST:
        #     register_form = RegisterUserForm(request.POST)
        #     if register_form.is_valid():
        #         print('if valid register')
        #         cd = register_form.cleaned_data
        #         user = authenticate(request, username = cd['username'], password = cd['password'])
        #         # перевірка чи користувач є і чи він не забанений
        #         if user and user.is_active:
        #             login(request, user)
        #             print('форма регістер')
        #             return HttpResponseRedirect(reverse('main'))
    else:
        login_form = LoginUserForm()
        # register_form = RegisterUserForm()
    return render(request, 'main/main.html', context={'login_form': login_form,
                                                    #   'register_form': register_form
                                                    })
    
