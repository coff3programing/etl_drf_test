# Generated by Django 5.0.7 on 2024-10-08 02:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('levels', '0002_levelsuploadfilesmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadAgronomicosFilesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='address')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('levels', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levels.levelsmodel')),
            ],
            options={
                'verbose_name': 'upload agronomico',
                'verbose_name_plural': 'upload agronomicos',
                'db_table': 'upload agronomicos',
            },
        ),
    ]
