# Generated by Django 4.2.3 on 2023-07-17 17:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0006_rename_name_postcomments_naam_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomments',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 17, 23, 23, 45, 116691)),
        ),
        migrations.AlterField(
            model_name='property',
            name='price',
            field=models.FloatField(max_length=50),
        ),
    ]
