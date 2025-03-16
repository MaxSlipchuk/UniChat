from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.http.response import HttpResponseNotFound, HttpResponse
from django.template.loader import render_to_string

# Create your views here.

# клас для відображення сторінки
class UsersPage(View):
    # для обробки get
    def get(self, request):
        return render(request, 'users/users.html')

    # для обробки post
    def post(self, request):
        print("форма відпрвлена")
        return render(request, 'main/main.html')


def login_user(request):
    return HttpResponse('login')

def logout_user(request):
    return HttpResponse('logout')




# class Account(View):
#     # для обробки get
#     def get(self, request):
#         return render(request, 'account/account.html')
    
#     # для обробки post
#     def post(self, request):
#         print("форма відпрвлена")
#         return render(request, 'account/account.html')

    

    
