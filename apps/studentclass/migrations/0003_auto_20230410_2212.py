# Generated by Django 3.2.6 on 2023-04-10 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('establishment', '0003_remove_establishment_deleted'),
        ('studentclass', '0002_alter_class_options_alter_class_establishment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='deleted',
        ),
        migrations.AlterField(
            model_name='class',
            name='establishment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='class_establishment', to='establishment.establishment', verbose_name='Школа'),
        ),
    ]
