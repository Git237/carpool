# Generated by Django 3.0.6 on 2021-03-29 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0002_relationship'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regdriver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('contact', models.CharField(max_length=10, null=True)),
                ('model', models.CharField(max_length=20, null=True)),
                ('capcity', models.CharField(max_length=20, null=True)),
                ('f1', models.ImageField(upload_to='')),
            ],
        ),
    ]
