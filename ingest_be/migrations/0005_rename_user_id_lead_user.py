# Generated by Django 5.1.6 on 2025-02-10 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ingest_be', '0004_lead_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lead',
            old_name='user_id',
            new_name='user',
        ),
    ]
