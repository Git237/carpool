# Generated by Django 3.0.6 on 2021-04-01 08:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('driver2', '0006_carformmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carformmodel',
            name='type',
        ),
        migrations.AddField(
            model_name='carformmodel',
            name='fare',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='carformmodel',
            name='journey_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
