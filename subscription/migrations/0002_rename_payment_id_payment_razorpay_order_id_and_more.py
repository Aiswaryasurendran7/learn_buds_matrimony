# Generated by Django 5.0.8 on 2024-09-07 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='payment_id',
            new_name='razorpay_order_id',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='order_id',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='user',
        ),
        migrations.AddField(
            model_name='payment',
            name='razorpay_payment_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='razorpay_signature',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(default='PENDING', max_length=20),
        ),
    ]
