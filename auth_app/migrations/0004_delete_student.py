# Generated by Django 5.1.3 on 2024-11-28 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0003_student'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
    ]