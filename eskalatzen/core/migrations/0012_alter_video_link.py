# Generated by Django 4.0.4 on 2022-05-28 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='link',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='link'),
        ),
    ]
