# Generated by Django 3.2.7 on 2021-10-01 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cessions', '0015_alter_cession_agency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cession',
            name='publishing_company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cessions.publishing_company'),
        ),
    ]