# Generated by Django 2.0 on 2018-01-31 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_management', '0015_order_sup_allo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_sup_allo',
            name='clear_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='order_sup_allo',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]