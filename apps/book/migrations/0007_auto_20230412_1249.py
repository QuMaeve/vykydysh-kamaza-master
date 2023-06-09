# Generated by Django 3.2.6 on 2023-04-12 03:49

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_auto_20230412_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_path',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/media/'), upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='doc_path',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/media/'), upload_to='documents/'),
        ),
    ]
