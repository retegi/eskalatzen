# Generated by Django 4.0.4 on 2022-06-10 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_climbingspot_locid_climbingspot_regionid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='climbingspot',
            name='enable',
            field=models.BooleanField(blank=True, null=True, verbose_name='jatorria'),
        ),
    ]
