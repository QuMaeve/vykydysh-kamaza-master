from django import forms
from apps.user.models import CustomUser

class ImportForm(forms.ModelForm):
    file = forms.FileField(
        label='Выберите файл',
        required=False,
        widget=forms.FileInput(
            attrs={
                "placeholder": "Выберите файл",
                "class": "form-control",
            }
        )
    )
    
    class Meta:
            model = CustomUser
            fields = ['file',]
          