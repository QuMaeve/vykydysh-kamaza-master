# Generated by Django 3.2.6 on 2023-04-12 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_remove_book_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_path',
            field=models.FileField(blank=True, null=True, upload_to='media/documents/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='doc_path',
            field=models.FileField(blank=True, null=True, upload_to='media/documents/'),
        ),
    ]
