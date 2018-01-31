# Generated by Django 2.0 on 2018-01-31 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_management', '0005_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='ORDER',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('No', models.CharField(max_length=12, unique=True)),
                ('status', models.SmallIntegerField()),
                ('client_id', models.IntegerField()),
                ('cargo_quantity', models.IntegerField()),
                ('receiveables', models.FloatField(null=True)),
                ('received', models.FloatField(null=True)),
                ('create_time', models.DateField(null=True)),
                ('clear_time', models.DateField(null=True)),
                ('if_delete', models.SmallIntegerField()),
            ],
            options={
                'permissions': (('view_order', 'Can access information of orders'), ('view_trash_order', 'Can access information of trash box')),
            },
        ),
    ]