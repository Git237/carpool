# Generated by Django 3.0.6 on 2021-04-03 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver2', '0008_auto_20210402_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carformmodel',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='carformmodel',
            name='journey_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='carformmodel',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]