# Generated by Django 4.0 on 2025-01-20 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rename_bankdetails_bank_master_bankaddress_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_bank',
            name='dob',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_bank',
            name='gender',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
    ]
