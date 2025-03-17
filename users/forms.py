from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

class LoginUserForm(forms.Form):
    username = forms.CharField(label='Логін', 
                               widget = forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', 
                               widget = forms.PasswordInput(attrs={'class': 'form-input'}))
    


# class LoginUserForm(AuthenticationForm):
    # username = forms.CharField(label='Логін', 
    #                            widget = forms.TextInput(attrs={'class': 'form-input'}))
    # password = forms.CharField(label='Пароль', 
    #                            widget = forms.PasswordInput(attrs={'class': 'form-input'}))

    # class Meta:
    #     # отримати поточну модель користувача
    #     user = get_user_model()
    #     fields = ['username', 'password']



class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label='Логін', 
                               widget = forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='E-mail',
                             widget = forms.EmailInput(attrs={'class': 'form-input'}))

    password = forms.CharField(label='Пароль', 
                               widget = forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Підтвердження пароля', 
                               widget = forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        user = get_user_model()
        fields = ['username', 'email', 'password', 'password2']
        labels = {
            'email': 'E-mail'
        }