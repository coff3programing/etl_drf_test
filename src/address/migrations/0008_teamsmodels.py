# Generated by Django 5.0.7 on 2024-10-05 18:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0007_alter_addressmodel_parroquia'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamsModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100)),
                ('team_lider_name', models.CharField(max_length=75)),
                ('team_description', models.TextField()),
                ('image', models.ImageField(upload_to='teams')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.addressmodel')),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
                'db_table': 'teams',
            },
        ),
    ]
