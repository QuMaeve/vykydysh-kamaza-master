# Generated by Django 3.2.6 on 2023-04-05 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_customuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='cleaned_password',
            field=models.CharField(max_length=150, null=True, verbose_name='Пароль исходный'),
        ),
    ]
