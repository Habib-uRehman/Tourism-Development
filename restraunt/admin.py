from django.contrib import admin
from . models import restraunt , ownership , manager ,furniture_dining , furniture_kitchen
from .models import Author, Book
# Register your models here.
admin.site.register(restraunt)
admin.site.register(ownership)
admin.site.register(manager)
admin.site.register(furniture_dining)
admin.site.register(furniture_kitchen)


class BookInLineAdmin(admin.TabularInline):
    model = Book


class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInLineAdmin]


admin.site.register(Author, AuthorAdmin)