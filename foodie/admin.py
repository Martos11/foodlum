from django.contrib import admin
from . models import *

# Register your models here.

class VarietyAdmin(admin.ModelAdmin):
    list_display = ('id','name','slug','image','created','updated')
    list_display_links = ['id','name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Variety, VarietyAdmin)
    
    
class MealAdmin(admin.ModelAdmin):
    list_display = ('id','variety','meal','slug','menu','image','spicy','time','price','discount','min_order','max_order','breakfast','lunch','dinner','display','created','updated')
    list_display_links = ['id','variety','slug','meal']
    list_editable = ['display','discount','price']
    prepopulated_fields = {'slug':('meal',)}
    
admin.site.register(Meal, MealAdmin)


