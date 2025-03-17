from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

# для виправлення помилки
app_name = 'users'

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    # path('logout/', LogoutView.as_view(), name='logout'),
]