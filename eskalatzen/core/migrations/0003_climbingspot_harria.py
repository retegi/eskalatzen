# Generated by Django 4.0.4 on 2022-05-13 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_climbingspot_link_climbingspot_image4_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='climbingspot',
            name='Harria',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Autonomi erkidegoa'),
        ),
    ]
