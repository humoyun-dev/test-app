# Generated by Django 5.0.2 on 2024-03-04 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='user',
        ),
    ]
