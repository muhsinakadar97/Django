# Generated by Django 4.1.7 on 2023-09-19 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_mymodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]