from django import forms
from apps.user.models import CustomUser
from apps.establishment.models import Establishment
from .models import Issue

class IssueUserForm(forms.ModelForm):
    student = forms.ModelMultipleChoiceField(
        label='Ученики',
        required=False,
        queryset=CustomUser.objects.filter(groups__name='Ученики'),
        widget=forms.SelectMultiple(
            attrs={
                "placeholder": "Ученики",
                "class": "form-control search-select "
            }
        )
    )
    def __init__(self, user, *args, **kwargs):
        super(IssueUserForm, self).__init__(*args, **kwargs)
        if user.establishment:
            print(user.establishment)
            self.fields['student'].queryset = CustomUser.objects.filter(
                establishment=Establishment.objects.get(id=user.establishment.id),
                groups__name='Ученики')
        else:
            print('else')
            self.fields['student'].queryset = CustomUser.objects.filter(
                groups__name='Ученики')
           
    class Meta:
            model = Issue
            fields = "__all__"

class IssueReportForm(forms.ModelForm):
    start_period = forms.DateField(
        label='Начало периода',
        required=False,
        widget=forms.DateInput(
            attrs={
                "placeholder": "Начало периода",
                "class": "form-control",
                'type': 'date'
            }
        )
    )
    end_period = forms.DateField(
        label='Конец периода',
        required=False,
        widget=forms.DateInput(
            attrs={
                "placeholder": "Конец периода",
                "class": "form-control",
                'type': 'date'
            }
        )
    ) 

    class Meta:
            model = Issue
            fields = "__all__"

class FilterIssueUserForm(forms.Form):
    sort_by = forms.ChoiceField(
        required=False,
        label="Сортировать",
        choices=[
            ('-id', 'Сортировать по умолчанию'),
            ('name', 'Сортировать по наименованию от А до Я'),
            ('-name', 'Сортировать по наименованию от Я до А'),
        ],
        widget=forms.Select(
            attrs={
                "class": "form-select"
            }
        ),
    )
    sort_name = forms.CharField(
        required=False,
        label="Поиск",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Поиск по ученикам",
                "class": "form-control"
            }
        )
    )
# Школа - Класс - ФИО