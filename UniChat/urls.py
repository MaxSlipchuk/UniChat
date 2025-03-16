"""
URL configuration for UniChat project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users.views import UsersPage
from app_base.views import page_not_found
from main.views import MainPage
# from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # users/login - правильний шлях
    path('users/', include('users.urls', namespace='users')),
    path('', UsersPage.as_view(), name='account_page'),
    path('main/', MainPage.as_view(), name='main'),
]

# для сторінок яких не існує
handler404 = page_not_found