# Generated by Django 3.0.6 on 2021-04-27 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver2', '0024_auto_20210427_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carformmodel',
            name='start_time',
            field=models.TimeField(max_length=30),
        ),
    ]
