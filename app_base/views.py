from django.shortcuts import render
from django.http.response import HttpResponseNotFound

# Create your views here.

# для сторінок яких не існує
def page_not_found(request, exception):
    # return HttpResponseNotFound('<h1>Сторінка не знайдена</h1>')
    return render(request, 'app_base/404.html')