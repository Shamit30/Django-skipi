# Generated by Django 3.2.8 on 2021-11-19 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skipimovie', '0002_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]
