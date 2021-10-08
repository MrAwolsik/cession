# Generated by Django 3.2.7 on 2021-09-27 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cessions', '0005_remove_publishing_company_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agent',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='publisher_contact',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='publisher_contact',
            name='last_name',
        ),
    ]