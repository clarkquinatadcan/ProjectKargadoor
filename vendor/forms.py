from django import forms


from django.contrib.auth import (
        authenticate,
        get_user_model,
        login,
        logout,
    )


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput) 
