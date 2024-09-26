# Generated by Django 5.0.8 on 2024-09-12 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('U_auth', '0025_userpersonaldetails_bio'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country_codes',
            options={'ordering': ['calling_code']},
        ),
        migrations.RenameField(
            model_name='country_codes',
            old_name='country_code',
            new_name='calling_code',
        ),
        migrations.AlterField(
            model_name='userpersonaldetails',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default_pic.png', upload_to='images/'),
        ),
    ]
