# Generated by Django 2.0 on 2018-02-12 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order_management', '0024_auto_20180212_0227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='receiveables',
        ),
        migrations.RemoveField(
            model_name='order',
            name='received',
        ),
    ]