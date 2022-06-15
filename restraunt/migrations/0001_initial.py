# Generated by Django 3.2 on 2022-06-08 19:04

import datetime
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='furniture_dining',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('furniture_type', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='furniture_kitchen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('furniture_type', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_manager', models.CharField(max_length=20, null=True)),
                ('manager_percent', models.IntegerField(null=True)),
                ('manager_address', models.TextField(max_length=100, null=True)),
                ('manager_telephone', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ownership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_owner', models.CharField(max_length=100, null=True)),
                ('owner_percent', models.IntegerField(null=True)),
                ('owner_address', models.TextField(max_length=100, null=True)),
                ('telegraphic_address', models.TextField(max_length=100, null=True)),
                ('owner_telephone', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='restraunt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restraunt_name', models.CharField(max_length=100)),
                ('establisment_date', models.DateField(default=datetime.date.today)),
                ('commission_date', models.DateField(default=datetime.date.today)),
                ('telex_num', models.IntegerField(default=1)),
                ('telephone_num', models.IntegerField(default=1)),
                ('address', models.TextField(default=1, max_length=100)),
                ('telegraphic_num', models.IntegerField(default=1)),
                ('province', models.CharField(choices=[('balochistan', 'BALOCHISTAN'), ('punjab', 'PUNJAB'), ('sindh', 'SINDH'), ('kpk', 'KPK'), ('fata', 'FATA')], default='green', max_length=100)),
                ('town', models.CharField(max_length=20, null=True)),
                ('street', models.CharField(max_length=100, null=True)),
                ('ownership', models.CharField(choices=[('proprietary', 'Proprietary'), ('partnership', 'Partnership'), ('private company', 'Private Company'), ('limited', 'Limited'), ('unlimited', 'Unlimited')], max_length=100, null=True)),
                ('total_area', models.IntegerField(null=True)),
                ('area_of_kitchen', models.IntegerField(null=True)),
                ('area_of_dining', models.IntegerField(null=True)),
                ('seating_area', models.IntegerField(null=True)),
                ('cost_of_furniture', models.IntegerField(default=1, null=True)),
                ('cost_of_equipment', models.IntegerField(null=True)),
                ('annual_rent', models.IntegerField(null=True)),
                ('working_capital', models.IntegerField(null=True)),
                ('number_of_floors', models.IntegerField(null=True)),
                ('number_of_room', models.IntegerField(null=True)),
                ('nature_of_room', models.CharField(choices=[('single bed room', 'SINGLE BED ROOM'), ('double bed room', 'DOUBLE BED ROOM'), ('suite room', 'SUITE ROOM')], max_length=100, null=True)),
                ('available_facilities', multiselectfield.db.fields.MultiSelectField(choices=[('reception', 'RECEPTION'), ('bill counter', 'BILL COUNTER'), ('telephone', 'TELEPHONE'), ('air-condition', 'AIR-CONDITION'), ('heating', 'HEATING'), ('cloak room', 'CLOAK ROOM'), ('toilet', 'TOILET'), ('car park', 'CAR PARK'), ('entertainment', 'ENTERTAINMENT')], max_length=95, null=True)),
                ('type_of_cuisine', models.CharField(max_length=100, null=True)),
                ('total_investment', models.IntegerField(null=True)),
                ('total_number_mangers', models.IntegerField(null=True)),
                ('total_number_receptionists', models.IntegerField(null=True)),
                ('total_number_billers', models.IntegerField(null=True)),
                ('total_number_cooks', models.IntegerField(null=True)),
                ('name_of_designation', models.CharField(max_length=100, null=True)),
                ('total_number_bearers', models.IntegerField(null=True)),
                ('professionally_trained', models.IntegerField(null=True)),
                ('not_professionally', models.IntegerField(null=True)),
                ('apprentices', models.IntegerField(null=True)),
                ('english_knowing', models.IntegerField(null=True)),
                ('rates', models.CharField(choices=[('immeidiatly', 'IMMEIDIATLY'), ('after dinner', 'AFTER DINNER')], max_length=100, null=True)),
            ],
        ),
    ]
