# Generated by Django 3.1.5 on 2021-02-20 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_auto_20210220_0846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasker',
            name='rating',
        ),
    ]