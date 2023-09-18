# Generated by Django 4.1.5 on 2023-01-22 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_transaction_details_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction_details',
            name='status_for_reciever',
            field=models.CharField(choices=[('debit', 'Debit'), ('credit', 'Credit'), ('none', 'None')], default='none', max_length=6),
        ),
        migrations.AddField(
            model_name='transaction_details',
            name='status_for_sender',
            field=models.CharField(choices=[('debit', 'Debit'), ('credit', 'Credit'), ('none', 'None')], default='none', max_length=6),
        ),
    ]
