# Generated by Django 4.0.1 on 2022-04-25 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restraunt', '0006_remove_restraunt_commission_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restraunt',
            name='address',
        ),
        migrations.RemoveField(
            model_name='restraunt',
            name='telegraphic_num',
        ),
        migrations.RemoveField(
            model_name='restraunt',
            name='telephone_num',
        ),
    ]
