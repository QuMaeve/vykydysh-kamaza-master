# Generated by Django 3.2.6 on 2023-04-10 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0002_alter_author_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='deleted',
        ),
    ]
