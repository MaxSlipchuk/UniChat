from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model

class LoginUserForm(forms.Form):
    username = forms.CharField(label='Логін', 
                               widget = forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', 
                               widget = forms.PasswordInput(attrs={'class': 'form-input'}))
    


# class LoginUserForm(AuthenticationForm):
#     username = forms.CharField(label='Логін', 
#                                widget = forms.TextInput(attrs={'class': 'form-input'}))
#     password = forms.CharField(label='Пароль', 
#                                widget = forms.PasswordInput(attrs={'class': 'form-input'}))

#     class Meta:
#         # отримати поточну модель користувача
#         user = get_user_model()
#         fields = ['username', 'password']


# class LoginUserForm(forms.ModelForm):
#     username = forms.CharField(label='Логін', 
#                                widget = forms.TextInput(attrs={'class': 'form-input'}))
#     password = forms.CharField(label='Пароль', 
#                                widget = forms.PasswordInput(attrs={'class': 'form-input'}))

#     class Meta:
#         # отримати поточну модель користувача
#         model = get_user_model()
#         fields = ['username', 'password']



# class RegisterUserForm(forms.ModelForm):
#     username = forms.CharField(label = 'Логін', 
#                                widget = forms.TextInput(attrs={'class': 'form-input'}))
#     email = forms.EmailField(label = 'E-mail',
#                              required = False,
#                              widget = forms.EmailInput(attrs={'class': 'form-input'}))

#     password = forms.CharField(label='Пароль', 
#                                widget = forms.PasswordInput(attrs={'class': 'form-input'}))
#     password2 = forms.CharField(label ='Підтвердження пароля', 
#                                widget = forms.PasswordInput(attrs={'class': 'form-input'}))

#     class Meta:
#         model = get_user_model()
#         fields = ['username', 'email', 'password', 'password2']
#         labels = {
#             'email': 'E-mail'
#         }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Логін", max_length=15)
    email = forms.EmailField(label = 'Email', required = False)
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Підтвердження паролю", widget=forms.PasswordInput)


    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control',
                'placeholder': self.fields[field_name].label
            })
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Паролі не співпадають")
        return password2



# class RegisterUserForm(forms.Form):
    # username = forms.CharField(label='Логін', 
                            #    widget = forms.TextInput(attrs={'class': 'form-input'}))
    # email = forms.EmailField(label='E-mail',
    #                          widget = forms.EmailInput(attrs={'class': 'form-input'}))

    # password = forms.CharField(label='Пароль', 
    #                            widget = forms.PasswordInput(attrs={'class': 'form-input'}))
    # password2 = forms.CharField(label='Підтвердження пароля', 
    #                            widget = forms.PasswordInput(attrs={'class': 'form-input'}))

    # class Meta:
    #     user = get_user_model()
    #     fields = ['username', 'email', 'password', 'password2']
    #     labels = {
    #         'email': 'E-mail'
    #     }