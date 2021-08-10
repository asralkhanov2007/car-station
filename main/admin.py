from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
	list_display = ['name', 'id']
	list_display_links = ['name']		


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
	list_display = ['title', 'id']
	list_display_links = ['title']	
	prepopulated_fields = {'slug':('title',)}

@admin.register(TransportCategory)
class TransportCategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'id']
	list_display_links = ['name']	
	prepopulated_fields = {'slug':('name',)}

@admin.register(BusGrafik)
class BusGrafikAdmin(admin.ModelAdmin):
	list_display = ['city', 'id']
	list_display_links = ['city']	
	prepopulated_fields = {'slug':('city',)}

@admin.register(FortGrafik)
class FortGrafikAdmin(admin.ModelAdmin):
	list_display = ['city', 'id']
	list_display_links = ['city']	
	prepopulated_fields = {'slug':('city',)}

@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
	list_display = ['name','category','id']
	list_display_links = ['name']	
	prepopulated_fields = {'slug':('name',)}