# Generated by Django 5.0.7 on 2024-10-07 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LevelsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_one', models.CharField(max_length=100)),
                ('field_two', models.CharField(max_length=100)),
                ('field_three', models.CharField(max_length=100)),
                ('field_four', models.CharField(max_length=100)),
                ('field_five', models.CharField(max_length=100)),
                ('field_six', models.CharField(max_length=100)),
                ('field_seven', models.CharField(max_length=100)),
                ('field_eight', models.CharField(max_length=100)),
                ('field_nine', models.CharField(max_length=100)),
                ('field_ten', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
