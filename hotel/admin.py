from django.contrib import admin
from .models import HotelOwner, HotelManager, CommonBathroom, CommonToilet, HotelRegistration

admin.site.register(HotelOwner)
admin.site.register(HotelManager)
admin.site.register(CommonBathroom)
admin.site.register(CommonToilet)
admin.site.register(HotelRegistration)
