from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.http.response import HttpResponseNotFound

# Create your views here.

# клас для відображення сторінки
class AccountPage(TemplateView):
    template_name = 'account/account.html'
    # для додавання додаткових данних

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'login'
        return context

    # для обробки post
    def post(self, request):
        print("форма відпрвлена")
        return render(request, 'account/account.html')
    


# class Account(View):
#     # для обробки get
#     def get(self, request):
#         return render(request, 'account/account.html')
    
#     # для обробки post
#     def post(self, request):
#         print("форма відпрвлена")
#         return render(request, 'account/account.html')

    

    
