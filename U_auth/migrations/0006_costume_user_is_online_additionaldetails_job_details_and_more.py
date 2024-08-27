# Generated by Django 5.0.8 on 2024-08-25 17:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('U_auth', '0005_otp_is_validated'),
    ]

    operations = [
        migrations.AddField(
            model_name='costume_user',
            name='is_online',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='AdditionalDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_married', models.BooleanField(default=False)),
                ('auual_income', models.BigIntegerField()),
                ('family_type', models.CharField(max_length=50)),
                ('family_name', models.CharField(max_length=50)),
                ('father_name', models.CharField(max_length=50)),
                ('father_occupation', models.CharField(max_length=50)),
                ('mother_name', models.CharField(max_length=50)),
                ('mother_occupation', models.CharField(max_length=50)),
                ('total_siblings', models.IntegerField()),
                ('total_siblings_married', models.IntegerField()),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('blood_group', models.CharField(max_length=50)),
                ('religion', models.CharField(max_length=50)),
                ('caste_or_community', models.CharField(max_length=50)),
                ('complexion', models.CharField(max_length=50, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Additional Detail',
                'verbose_name_plural': 'Additional Details',
            },
        ),
        migrations.CreateModel(
            name='Job_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('experiences_level', models.CharField(choices=[('entry', 'Entry Level'), ('mid', 'Mid Level'), ('senior', 'Senior Level')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Relationship_Goals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_short', models.BooleanField(default=False)),
                ('is_long', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserDisabilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disability_type', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='U_auth.additionaldetails')),
            ],
        ),
        migrations.CreateModel(
            name='UserPersonalDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=10)),
                ('dob', models.DateField()),
                ('smoking_habits', models.BooleanField(default=False, verbose_name='Smoking Habits')),
                ('drinking_habits', models.BooleanField(default=False, verbose_name='Drinking Habits')),
                ('profile_pic', models.ImageField(blank=True, default='img/default_pic.png', upload_to='images/')),
                ('short_video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('is_employer', models.BooleanField(default=False)),
                ('is_employee', models.BooleanField(default=False)),
                ('is_jobseeker', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_details', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Personal Detail',
                'verbose_name_plural': 'User Personal Details',
            },
        ),
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photos', models.ImageField(upload_to='images/')),
                ('add_at', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='U_auth.userpersonaldetails', verbose_name='reverse_user_pic')),
            ],
        ),
        migrations.CreateModel(
            name='Intrestes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intrest', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='U_auth.userpersonaldetails')),
            ],
        ),
        migrations.CreateModel(
            name='Hobbies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobby', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='U_auth.userpersonaldetails')),
            ],
        ),
    ]
