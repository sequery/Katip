from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from users.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=64, help_text = "Required, add a valid Email Address.", widget = forms.TextInput(attrs = {'class': 'form-control'}))
    username = forms.CharField(max_length=100, help_text = "Required, add a valid Username. ", widget = forms.TextInput(attrs = {'class': 'form-control'}))


    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2', ]


class UserAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label = "Password", widget = forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['email', 'password',]

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid Login")


class UserEditForm(forms.ModelForm):
    email = forms.EmailField(max_length=64, widget = forms.TextInput(attrs = {'class': 'form-control form-control-lg','placeholder' : 'Enter Email'}))
    username = forms.CharField(max_length=100, widget = forms.TextInput(attrs = {'class': 'form-control form-control-lg','placeholder' : 'Enter Email'}))

    class Meta:
        model = User
        fields = ['email', 'username', 'admin', 'staff', 'active', 'confirmed']