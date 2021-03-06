# Generated by Django 3.1a1 on 2020-05-17 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20200517_0431'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='amenity',
            options={'verbose_name_plural': 'Amenities'},
        ),
        migrations.AlterModelOptions(
            name='facility',
            options={'verbose_name_plural': 'Facilities'},
        ),
        migrations.AlterModelOptions(
            name='houserule',
            options={'verbose_name': 'House Rule'},
        ),
        migrations.AlterModelOptions(
            name='roomtype',
            options={'verbose_name': 'Room Type'},
        ),
        migrations.AlterField(
            model_name='room',
            name='aminity',
            field=models.ManyToManyField(blank=True, to='rooms.Amenity'),
        ),
        migrations.AlterField(
            model_name='room',
            name='facility',
            field=models.ManyToManyField(blank=True, to='rooms.Facility'),
        ),
        migrations.AlterField(
            model_name='room',
            name='houserule',
            field=models.ManyToManyField(blank=True, to='rooms.HouseRule'),
        ),
    ]
