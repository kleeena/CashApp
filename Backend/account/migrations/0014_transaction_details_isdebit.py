# Generated by Django 4.1.5 on 2023-01-22 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_rename_transaction_time_transaction_details_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction_details',
            name='isDebit',
            field=models.BooleanField(default=False),
        ),
    ]