# Generated by Django 3.1.5 on 2021-02-20 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_auto_20210220_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasker',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=1, null=True),
        ),
    ]