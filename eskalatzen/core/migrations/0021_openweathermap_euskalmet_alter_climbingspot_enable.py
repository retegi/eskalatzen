# Generated by Django 4.0.4 on 2022-06-10 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_climbingspot_enable'),
    ]

    operations = [
        migrations.AddField(
            model_name='openweathermap',
            name='euskalmet',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='euskalmet icon'),
        ),
        migrations.AlterField(
            model_name='climbingspot',
            name='enable',
            field=models.BooleanField(blank=True, null=True, verbose_name='enable'),
        ),
    ]
