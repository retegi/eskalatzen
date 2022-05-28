# Generated by Django 4.0.4 on 2022-05-28 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_camping_title_alter_camping_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Izena')),
                ('town', models.CharField(blank=True, max_length=200, null=True, verbose_name='Herria')),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='Helbidea')),
                ('website', models.CharField(blank=True, max_length=200, null=True, verbose_name='Web orria')),
                ('phone', models.CharField(blank=True, max_length=200, null=True, verbose_name='Telefono zenbakia')),
                ('desc', models.CharField(blank=True, max_length=200, null=True, verbose_name='Deskribapena')),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='Latitudea')),
                ('longitude', models.FloatField(blank=True, null=True, verbose_name='Longitudea')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Sortze data')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Edizio data')),
            ],
            options={
                'verbose_name': 'Material alokairua',
                'verbose_name_plural': 'Material alokairua',
                'ordering': ['created'],
            },
        ),
        migrations.AddField(
            model_name='camping',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Helbidea'),
        ),
        migrations.AddField(
            model_name='camping',
            name='phone',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Telefono zenbakia'),
        ),
        migrations.AddField(
            model_name='camping',
            name='website',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Web orria'),
        ),
    ]
