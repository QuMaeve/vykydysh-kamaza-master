# Generated by Django 4.1.6 on 2023-03-11 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=150, null=True)),
                ('last_name', models.CharField(blank=True, max_length=150, null=True)),
                ('patronymic', models.CharField(blank=True, max_length=150, null=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('deleted', models.BooleanField(default=0)),
            ],
        ),
    ]
