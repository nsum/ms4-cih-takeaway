# Generated by Django 3.2 on 2021-08-14 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210812_2131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='updated_on',
        ),
    ]