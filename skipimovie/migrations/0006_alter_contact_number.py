# Generated by Django 3.2.8 on 2021-11-19 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skipimovie', '0005_auto_20211120_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='number',
            field=models.CharField(default='', max_length=10),
        ),
    ]
