# Generated by Django 3.0.6 on 2021-04-03 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver2', '0013_bikeformmodel_license'),
    ]

    operations = [
        migrations.AddField(
            model_name='carformmodel',
            name='license',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]