# Generated by Django 3.2.8 on 2021-12-28 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendorPortal', '0010_rename_given_input_vendorlogin_vendor_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='Feedback',
        ),
    ]
