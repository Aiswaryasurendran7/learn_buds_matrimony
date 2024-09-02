# Generated by Django 5.0.8 on 2024-09-02 16:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('U_auth', '0022_interest_and_hobbie_lifestylechoice_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job_details',
            name='location',
        ),
        migrations.RemoveField(
            model_name='location',
            name='user',
        ),
        migrations.AddField(
            model_name='job_details',
            name='job_location',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='U_auth.location'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='address_details',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='latitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='longitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userpersonaldetails',
            name='user_location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='U_auth.location'),
            preserve_default=False,
        ),
    ]
