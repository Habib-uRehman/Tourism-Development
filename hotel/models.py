from django.db import models




# Owner Class
class HotelOwner(models.Model):
    owner_name = models.CharField(max_length=30, null=True)
    owner_ratio = models.CharField(max_length=30, null=True)
    owner_full_address = models.CharField(max_length=200, null=True)
    owner_telegraphic_address = models.CharField(max_length=200, null=True)
    owner_telephone = models.CharField(max_length=15, null=True)
    # owner_id = models.ForeignKey(HotelRegistration, on_delete=models.CASCADE) # Owner Foreign Key to Hotel Registration


# Hotel Manager Class
class HotelManager(models.Model):
    manager_name = models.CharField(max_length=30, null=True)
    manager_ratio = models.CharField(max_length=30, null=True)
    manager_full_address = models.CharField(max_length=200, null=True)
    manager_telegraphic_address = models.CharField(max_length=200, null=True)
    manager_telephone = models.CharField(max_length=15, null=True)
    # manager_id = models.ForeignKey(HotelRegistration, on_delete=models.CASCADE) # manager foreign key attach to hotel registration

# Common Places Class
class CommonBathroom(models.Model):
    bathroom_no = models.CharField(max_length=10, null=True, blank=True) # Common Bathroom no
    bathroom_floor = models.CharField(max_length=20, null=True, blank=True) # Common Floor No
    
    # common_place_id = models.ForeignKey(HotelRegistration, on_delete=models.CASCADE) # common place foreign key attach to hotel registration
class CommonToilet(models.Model):
    toilet_no = models.CharField(max_length=10, null=True, blank=True) #Common Toilet No
    toilet_floor = models.CharField(max_length=20, null=True, blank=True) # Floor No
# Furniture and Fixtures
# class Bedroom(models.Model):
    bedrooms_type = models.CharField(max_length=100 , null=True) # Bedrooms
    # rooms_type = models.CharField(max_length=100, null=True) # Common Rooms
    # corridors_type = models.CharField(max_length=100, null=True) # Corridors and Galleries
    # attached_bathroom_type = models.CharField(max_length=100, null=True) # bathroom attached with bedrooms
    # bathrooms_type = models.CharField(max_length=100, null=True) # common bathrooms
    # toilets_type = models.CharField(max_length=100, null=True) # common toilots
    # cuisine_name = models.CharField(max_length=100, null=True) # cuisine served
    # furniture_id = models.ForeignKey(HotelRegistration, on_delete=models.CASCADE) # furniture foreign key attach to hotel registration
# class Rooms(models.Model):
#     rooms_type = models.CharField(max_length=100, null=True) # Common Rooms

# class Corridors(models.Model):
#     corridors_type = models.CharField(max_length=100, null=True) # Common Corridors

# class AttachedBathroom(models.Model):
#     attached_bathroom_type = models.CharField(max_length=100, null=True) # Common Attached Bathroom

# class Bathroom(models.Model):
#     common_bathroom_type = models.CharField(max_length=100, null=True) # Common Bathroom

# class Toilet(models.Model):
#     toilets_type = models.CharField(max_length=100, null=True) # common toilots

# class Cuisine(models.Model):
#     cuisine_name = models.CharField(max_length=100, null=True) # Common Cuisine

class HotelRegistration(models.Model):

    hotel_name = models.CharField(max_length=100) # Name of the hotel
    establishment_year = models.IntegerField(default=0) # year of establishment
    commision_date = models.DateField() # data of commission    
    telex_number = models.CharField(max_length=15) # Telex number
    phone_number = models.CharField(max_length=15) # Telephone Number
    hotel_address = models.CharField(max_length=100) # Address
    telegraphic_address = models.CharField(max_length=200) # Telegraphic Address

    # Location information
    province = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    street = models.CharField(max_length=100)

    # Land information
    hotel_area = models.CharField(max_length=100) # Area of Hotel
    covered_area = models.CharField(max_length=100) # Covered Area
    area_type = models.CharField(max_length=100) # Area Type

    # cost information
    land_cost = models.FloatField(default=0) # Cost of Land
    building_cost = models.FloatField(default=0) # Cost of building
    furniture_cost = models.FloatField(default=0) # cost of furniture & Fixtures
    equipment_cost = models.FloatField(default=0) # cost of equipment
    working_capital = models.FloatField(default=0) # working capital
    total_investment = models.FloatField(default=0)

    # Building information
    floor_numbers = models.IntegerField(default=0) # number of floors
    room_numbers = models.IntegerField(default=0) # Number of rooms on each floor

    
    NATURE_OF_ROOM = (
    ('single bed room','SINGLE BED ROOM'),
    ('double bed room', 'DOUBLE BED ROOM'),
    ('suite room','SUITE ROOM'),  
)
    room_nature = models.CharField(max_length=100)  # nature of room

    # Public Rooms
    visitor_room_detail = models.CharField(max_length=200, null=True)
    visitor_room_area = models.CharField(max_length=100, null=True)
    reception_hall_detail = models.CharField(max_length=200, null=True)
    reception_hall_area = models.CharField(max_length=100, null=True)
    cloak_room_detail = models.CharField(max_length=200, null=True)
    cloak_room_area = models.CharField(max_length=100, null=True)
    reading_room_detail = models.CharField(max_length=200, null=True)
    reading_room_area = models.CharField(max_length=100, null=True)
    restaurant_detail = models.CharField(max_length=200, null=True)
    restaurant_area = models.CharField(max_length=100, null=True)

    # Below from Common Toilets No
    staircase_no = models.IntegerField(default=0) # No. Of Staircase:
    lifts_no = models.IntegerField(default=0) # No. Of Lifts:
    car_park = models.CharField(max_length=20) # Car Park (Lease Indicate Capacity):
    area_of_compound  = models.CharField(max_length=30) # Area of Compund:
    area_of_garden = models.CharField(max_length=40, null=True) # Area Of Garden (If any):
    construction_completion_date = models.DateField() # Date of Completion of Construction :
    renovation_last_date = models.DateField(null=True, blank=True) # Last Date of Renovation (If Any):
    building_files = models.FileField(upload_to='building_files/', null=True, blank=True) # Please Attach a Plan of The Buildings


    # Is restaurant attached with hotel
    restaurant_name = models.CharField(max_length=100, null=True) # Restaurant Name
    restaurant_detail_files = models.FileField(upload_to='restaurant_files/', null=True) # Please Attach Restaurant Details


    # Foreighn Keys
    owner_id = models.ForeignKey(HotelOwner, on_delete=models.CASCADE)
    manager_id = models.ForeignKey(HotelManager, on_delete=models.CASCADE)
    common_bathroom_id = models.ForeignKey(CommonBathroom, on_delete=models.CASCADE)
    common_toilet_id = models.ForeignKey(CommonToilet, on_delete=models.CASCADE)
    # furniture_id = models.ForeignKey(FurnitureFixtures, on_delete=models.CASCADE)






    






