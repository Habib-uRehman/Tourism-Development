# Generated by Django 4.0.3 on 2022-04-04 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0004_alter_travelagency_exchange_statment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelagency',
            name='reside_in_pakistan',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')]),
        ),
    ]
