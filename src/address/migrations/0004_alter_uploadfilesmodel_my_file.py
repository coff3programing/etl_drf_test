# Generated by Django 5.0.7 on 2024-10-04 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0003_rename_uploadfiles_uploadfilesmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfilesmodel',
            name='my_file',
            field=models.FileField(upload_to='address'),
        ),
    ]
