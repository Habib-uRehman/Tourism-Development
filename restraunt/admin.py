from django.contrib import admin
from . models import restraunt , ownership , manager
# Register your models here.
admin.site.rigister(restraunt)
admin.site.rigister(ownership)
admin.site.rigister(manager)

