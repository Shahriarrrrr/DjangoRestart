# Generated by Django 5.1.4 on 2025-01-09 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('roll', models.IntegerField()),
                ('email', models.EmailField(max_length=255)),
                ('city', models.CharField(max_length=70)),
            ],
        ),
    ]
