# Generated by Django 3.2.7 on 2021-10-01 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cessions', '0011_cession_publishing_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cession',
            name='end_at',
            field=models.DateTimeField(null=True),
        ),
    ]
