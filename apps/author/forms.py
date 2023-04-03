from django import forms
from .models import Author


class AuthorForm(forms.ModelForm):
    first_name = forms.CharField(
        label='Имя',
        required=True,
        max_length=150,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Фамилия",
                "class": "form-control"
            }
        )
    )
    last_name = forms.CharField(
        label='Имя',
        required=True,
        max_length=150,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Имя",
                "class": "form-control"
            }
        )
    )
    patronymic = forms.CharField(
        label='Имя',
        required=False,
        max_length=150,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Имя",
                "class": "form-control"
            }
        )
    )
    description = forms.CharField(
        label='Описание',
        required=False,
        max_length=500,
        widget=forms.Textarea(
            attrs={
                "type":"text",
                "placeholder": "Описание",
                "class": "form-control form-control-sm",
                "rows":"3",
                "cols":"40",
            }
        )
    )

    class Meta:
        model = Author
        fields = [
                 'first_name',
                 'last_name',
                 'patronymic',
                 'description',
                 ]
