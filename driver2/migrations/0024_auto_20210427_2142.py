# Generated by Django 3.0.6 on 2021-04-27 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver2', '0023_auto_20210427_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carformmodel',
            name='start_time',
            field=models.DateField(max_length=30),
        ),
    ]