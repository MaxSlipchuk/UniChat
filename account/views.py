from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.http.response import HttpResponseNotFound
from django.template.loader import render_to_string

# Create your views here.

# клас для відображення сторінки
class AccountPage(View):
    # для обробки get
    def get(self, request):
        return render(request, 'account/account.html')

    # для обробки post
    def post(self, request):
        print("форма відпрвлена")
        return render(request, 'main/main.html')
    


# class Account(View):
#     # для обробки get
#     def get(self, request):
#         return render(request, 'account/account.html')
    
#     # для обробки post
#     def post(self, request):
#         print("форма відпрвлена")
#         return render(request, 'account/account.html')

    

    
