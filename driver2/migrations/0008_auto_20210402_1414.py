# Generated by Django 3.0.6 on 2021-04-02 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver2', '0007_auto_20210401_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carformmodel',
            name='date',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='carformmodel',
            name='journey_time',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='carformmodel',
            name='start_time',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
