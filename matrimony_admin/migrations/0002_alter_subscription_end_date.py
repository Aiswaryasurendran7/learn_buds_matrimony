# Generated by Django 5.0.8 on 2024-09-13 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrimony_admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='end_date',
            field=models.DateField(blank=True),
        ),
    ]
