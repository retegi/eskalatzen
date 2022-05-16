# Generated by Django 4.0.4 on 2022-05-13 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='climbingspot',
            name='link',
        ),
        migrations.AddField(
            model_name='climbingspot',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='projects', verbose_name='Irudia 4'),
        ),
        migrations.AlterField(
            model_name='climbingspot',
            name='ccaa',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Autonomi erkidegoa'),
        ),
        migrations.AlterField(
            model_name='climbingspot',
            name='country',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Herrialdea'),
        ),
        migrations.AlterField(
            model_name='climbingspot',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='projects', verbose_name='Irudia 1'),
        ),
        migrations.AlterField(
            model_name='climbingspot',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='projects', verbose_name='Irudia 2'),
        ),
        migrations.AlterField(
            model_name='climbingspot',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='projects', verbose_name='Irudia 3'),
        ),
        migrations.AlterField(
            model_name='climbingspot',
            name='latitude',
            field=models.FloatField(blank=True, null=True, verbose_name='Latitudea'),
        ),
        migrations.AlterField(
            model_name='climbingspot',
            name='longitude',
            field=models.FloatField(blank=True, null=True, verbose_name='Latitudea'),
        ),
        migrations.AlterField(
            model_name='climbingspot',
            name='province',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Probintzia'),
        ),
        migrations.AlterField(
            model_name='climbingspot',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Sektorea'),
        ),
        migrations.AlterField(
            model_name='climbingspot',
            name='town',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Herria'),
        ),
    ]
