# Generated by Django 4.1.6 on 2023-03-11 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('genre', models.CharField(blank=True, max_length=255, null=True)),
                ('count', models.IntegerField(blank=True, default=1000)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('doc_path', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('doc_url', models.CharField(blank=True, max_length=2048, null=True)),
                ('cover_path', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('cover_url', models.CharField(blank=True, max_length=2048, null=True)),
                ('deleted', models.BooleanField(default=0)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='book_author', to='author.author')),
            ],
        ),
    ]
