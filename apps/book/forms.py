from django import forms
from .models import Book
from apps.author.models import Author

class BookForm(forms.ModelForm):
    name = forms.CharField(
        label='Наименование книги',
        required=True,
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Наименование книги",
                "class": "form-control"
            }
        )
    )
    author = forms.ModelChoiceField(
        label="Автор",
        required=True,
        queryset=Author.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "form-select form-select-sm search-select"
            }
        ),
    )
    genre = forms.CharField(
        label='Жанр книги',
        required=False,
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Жанр книги",
                "class": "form-control"
            }
        )
    )
    count = forms.IntegerField(
        label='Количество книг',
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Количество книг",
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
                "rows":"2",
                "cols":"40",
            }
        )
    )
    doc_path = forms.FileField(
        label='Выберите файл книги',
        required=False,
        widget=forms.FileInput(
            attrs={
                "placeholder": "Выберите файл книги",
                "class": "form-control",
            }
        )
    )
    doc_url = forms.CharField(
        label='Ссылку на книгу',
        required=False,
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ссылка на книгу",
                "class": "form-control"
            }
        )
    )
    cover_path = forms.FileField(
        label='Выберите файл обложки',
        required=False,
        widget=forms.FileInput(
            attrs={
                "placeholder": "Выберите файл обложки",
                "class": "form-control"
            }
        )
    )
    cover_url = forms.CharField(
        label='Ссылку на обложку книги',
        required=False,
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ссылка на обложку книги",
                "class": "form-control"
            }
        )
    )
    class Meta:
            model = Book
            exclude = ('doc_path',)
            fields = [
                 'name',
                 'author',
                 'genre',
                 'count',
                 'description',
                 'doc_path',
                 'doc_url',
                 'cover_path',
                 'cover_url',
                 ]
            

class FilterBookForm(forms.Form):
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
                "placeholder": "Сортировать",
                "class": "form-select form-control-sm me-2"
            }
        ),
    )
    sort_name = forms.CharField(
        required=False,
        label="Поиск",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Поиск",
                "class": "form-control form-control-sm me-2", 
                "type":"search",
            }
        )
    )
