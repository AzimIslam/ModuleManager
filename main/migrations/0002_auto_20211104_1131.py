# Generated by Django 3.2.7 on 2021-11-04 11:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='created',
            field=models.DateField(default=datetime.datetime(2021, 11, 4, 11, 31, 24, 372508)),
        ),
        migrations.AddField(
            model_name='student',
            name='enrolled',
            field=models.DateField(default=datetime.datetime(2021, 11, 4, 11, 31, 24, 371508)),
        ),
    ]
