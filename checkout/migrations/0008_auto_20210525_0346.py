# Generated by Django 3.2 on 2021-05-25 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_auto_20210521_0421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pickup_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='pickup_time',
            field=models.TimeField(),
        ),
    ]
