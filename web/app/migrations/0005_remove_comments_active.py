# Generated by Django 3.1 on 2020-09-06 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200906_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='active',
        ),
    ]