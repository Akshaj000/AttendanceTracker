# Generated by Django 4.2.2 on 2023-07-03 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RefreshToken',
        ),
    ]