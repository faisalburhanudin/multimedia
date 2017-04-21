from django import forms


class UserRegisterForm(forms.Form):
    name = forms.CharField(label="Your name", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
