# Generated by Django 5.1.3 on 2024-11-29 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0005_alter_note_options_note_updated_at_alter_note_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
    ]