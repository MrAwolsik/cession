# Generated by Django 3.2.7 on 2021-09-27 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cessions', '0004_auto_20210928_0050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publishing_company',
            name='email',
        ),
    ]
