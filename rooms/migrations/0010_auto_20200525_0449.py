# Generated by Django 3.1a1 on 2020-05-25 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0009_auto_20200520_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='guests',
            field=models.IntegerField(help_text='How many people will be stay'),
        ),
    ]
