from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label="Usuário", max_length=12)
    password = forms.CharField(label="Usuário", max_length=20)
