# Generated by Django 3.0.6 on 2021-03-30 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('driver2', '0003_auto_20210330_1236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='regdriver',
            old_name='name',
            new_name='username',
        ),
    ]
