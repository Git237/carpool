# Generated by Django 3.0.6 on 2021-04-05 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('driver2', '0017_auto_20210404_1146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carformmodel',
            name='license',
        ),
    ]