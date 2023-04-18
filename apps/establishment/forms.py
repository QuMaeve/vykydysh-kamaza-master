from django import forms
from .models import Establishment
from apps.locality.models import Locality


class EstablishmentForm(forms.ModelForm):
    name = forms.CharField(
        label='Наименование учебного учреждения',
        required=True,
        max_length=500,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Наименование учебного учреждения",
                "class": "form-control"
            }
        )
    )
    contacts = forms.CharField(
        label='Контакты',
        required=False,
        max_length=500,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Контакты",
                "class": "form-control form-control-sm",
                "rows": "1"
            }
        )
    )
    address = forms.CharField(
        label='Адрес',
        required=False,
        max_length=500,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Адрес",
                "class": "form-control form-control-sm",
                "rows": "1"
            }
        )
    )
    requisites = forms.CharField(
        label='Реквизиты',
        required=False,
        max_length=500,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Реквизиты",
                "class": "form-control form-control-sm",
                "rows": "1"
            }
        )
    )

    locality = forms.ModelChoiceField(
        label="Принадлежность к территориальному образованию",
        required=False,
        queryset=Locality.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "form-select search-select"
            }
        ),
    )

    class Meta:
        model = Establishment
        fields = [
            'name',
            'contacts',
            'address',
            'requisites',
            'locality'
        ]


class FilterEstablishmentForm(forms.Form):
    sort_by = forms.ChoiceField(
        required=False,
        label="Сортировать",
        choices=[
            ('-id', 'Сортировать по умолчанию'),
            ('name', 'Сортировать по наименованию от А до Я'),
            ('-name', 'Сортировать по наименованию от Я до А'),
            ('locality', 'Сортировать по принадлежности от А до Я'),
            ('-locality', 'Сортировать по принадлежности от Я до А'),
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
                "placeholder": "Поиск по наименованию",
                "class": "form-control"
            }
        )
    )
