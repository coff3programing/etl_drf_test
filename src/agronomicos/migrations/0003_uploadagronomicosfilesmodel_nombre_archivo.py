# Generated by Django 5.0.7 on 2024-10-08 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agronomicos', '0002_alter_uploadagronomicosfilesmodel_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadagronomicosfilesmodel',
            name='nombre_archivo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
