# Generated by Django 4.1.6 on 2023-03-30 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
    ]
