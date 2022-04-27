# Generated by Django 4.0.3 on 2022-04-27 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommonBathroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bathroom_no', models.CharField(blank=True, max_length=10, null=True)),
                ('bathroom_floor', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CommonToilet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toilet_no', models.CharField(blank=True, max_length=10, null=True)),
                ('toilet_floor', models.CharField(blank=True, max_length=20, null=True)),
                ('bedrooms_type', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HotelManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager_name', models.CharField(max_length=30, null=True)),
                ('manager_ratio', models.CharField(max_length=30, null=True)),
                ('manager_full_address', models.CharField(max_length=200, null=True)),
                ('manager_telegraphic_address', models.CharField(max_length=200, null=True)),
                ('manager_telephone', models.CharField(max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HotelOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=30, null=True)),
                ('owner_ratio', models.CharField(max_length=30, null=True)),
                ('owner_full_address', models.CharField(max_length=200, null=True)),
                ('owner_telegraphic_address', models.CharField(max_length=200, null=True)),
                ('owner_telephone', models.CharField(max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HotelRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=100)),
                ('establishment_year', models.IntegerField(default=0)),
                ('commision_date', models.DateField()),
                ('telex_number', models.CharField(max_length=15)),
                ('phone_number', models.CharField(max_length=15)),
                ('hotel_address', models.CharField(max_length=100)),
                ('telegraphic_address', models.CharField(max_length=200)),
                ('province', models.CharField(max_length=100)),
                ('town', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('hotel_area', models.CharField(max_length=100)),
                ('covered_area', models.CharField(max_length=100)),
                ('area_type', models.CharField(max_length=100)),
                ('land_cost', models.FloatField(default=0)),
                ('building_cost', models.FloatField(default=0)),
                ('furniture_cost', models.FloatField(default=0)),
                ('equipment_cost', models.FloatField(default=0)),
                ('working_capital', models.FloatField(default=0)),
                ('total_investment', models.FloatField(default=0)),
                ('floor_numbers', models.IntegerField(default=0)),
                ('room_numbers', models.IntegerField(default=0)),
                ('room_nature', models.CharField(max_length=100)),
                ('visitor_room_detail', models.CharField(max_length=200, null=True)),
                ('visitor_room_area', models.CharField(max_length=100, null=True)),
                ('reception_hall_detail', models.CharField(max_length=200, null=True)),
                ('reception_hall_area', models.CharField(max_length=100, null=True)),
                ('cloak_room_detail', models.CharField(max_length=200, null=True)),
                ('cloak_room_area', models.CharField(max_length=100, null=True)),
                ('reading_room_detail', models.CharField(max_length=200, null=True)),
                ('reading_room_area', models.CharField(max_length=100, null=True)),
                ('restaurant_detail', models.CharField(max_length=200, null=True)),
                ('restaurant_area', models.CharField(max_length=100, null=True)),
                ('staircase_no', models.IntegerField(default=0)),
                ('lifts_no', models.IntegerField(default=0)),
                ('car_park', models.CharField(max_length=20)),
                ('area_of_compound', models.CharField(max_length=30)),
                ('area_of_garden', models.CharField(max_length=40, null=True)),
                ('construction_completion_date', models.DateField()),
                ('renovation_last_date', models.DateField(blank=True, null=True)),
                ('building_files', models.FileField(blank=True, null=True, upload_to='building_files/')),
                ('restaurant_name', models.CharField(max_length=100, null=True)),
                ('restaurant_detail_files', models.FileField(null=True, upload_to='restaurant_files/')),
                ('common_bathroom_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.commonbathroom')),
                ('common_toilet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.commontoilet')),
                ('manager_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.hotelmanager')),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.hotelowner')),
            ],
        ),
    ]