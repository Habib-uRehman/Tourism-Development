# Generated by Django 4.0.1 on 2022-04-25 16:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restraunt', '0003_auto_20220425_0517'),
    ]

    operations = [
        migrations.AddField(
            model_name='restraunt',
            name='address',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='restraunt',
            name='commission_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='restraunt',
            name='establisment_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='restraunt',
            name='restraunt_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='restraunt',
            name='telegraphic_num',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='restraunt',
            name='telephone_num',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='restraunt',
            name='telex_num',
            field=models.IntegerField(null=True),
        ),
    ]
