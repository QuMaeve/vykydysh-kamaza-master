from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Логин',
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Логин",
                "class": "login"
            }
        ))
    password = forms.CharField(
        label='Пароль',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Пароль",
                "class": "password"
            }
        ))
