# Generated by Django 3.1a1 on 2020-05-16 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200516_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthdate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='currency',
            field=models.CharField(blank=True, choices=[('USD', 'USD'), ('Ruppy', 'Ruppy')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='languate',
            field=models.CharField(choices=[('English', 'Englisth'), ('Hindi', 'Hindi'), ('Gujarati', 'Gujarati')], max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='superhost',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10, null=True),
        ),
    ]
