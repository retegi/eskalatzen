# Generated by Django 4.0.4 on 2022-05-29 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_openweathermap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openweathermap',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='projects', verbose_name='Icon'),
        ),
    ]
