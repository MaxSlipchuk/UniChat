from django.urls import path
from . import views

# для виправлення помилки
app_name = 'users'

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]