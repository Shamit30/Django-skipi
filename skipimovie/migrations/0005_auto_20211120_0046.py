# Generated by Django 3.2.8 on 2021-11-19 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skipimovie', '0004_auto_20211120_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]