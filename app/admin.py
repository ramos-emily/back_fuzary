from django.contrib import admin
from .models import *
# Register your models here.

class datSpell(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', )
    search_fields = ('name',)
    list_per_page = 10
    
admin.site.register(Spell, datSpell)

class datHouse(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', )
    search_fields = ('name',)
    list_per_page = 10
    
admin.site.register(House, datHouse)

class datCharacters(admin.ModelAdmin):
    list_display = ('name', 'house', 'wizard', 'species', 'eyecolors', 'haircolor', 'img')
    list_display_links = ('img', )
    search_fields = ('name',)
    list_per_page = 10
    
admin.site.register(Characters, datCharacters)

