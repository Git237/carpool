# Generated by Django 3.0.6 on 2021-03-29 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0003_regdriver'),
    ]

    operations = [
        migrations.RenameField(
            model_name='regdriver',
            old_name='capcity',
            new_name='capacity',
        ),
        migrations.RenameField(
            model_name='regdriver',
            old_name='f1',
            new_name='imgg',
        ),
    ]
