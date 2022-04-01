from django.contrib import admin

from .models import travelagency, assets, partner, manager, director

admin.site.register(travelagency)
admin.site.register(assets)
admin.site.register(partner)
admin.site.register(manager)
admin.site.register(director)


