# Generated by Django 3.2.8 on 2021-11-19 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skipimovie', '0006_alter_contact_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='msg_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]