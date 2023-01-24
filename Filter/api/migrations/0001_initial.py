# Generated by Django 4.1.3 on 2023-01-23 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('roll', models.IntegerField(unique=True)),
                ('city', models.CharField(max_length=100)),
                ('enrolled_by', models.CharField(max_length=100)),
            ],
        ),
    ]
