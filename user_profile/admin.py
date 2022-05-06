from django.contrib import admin
from . models import *

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display =('name','phone','subject','message','created','status','closed')
    
    
admin.site.register(Contact,ContactAdmin) 

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','first_name','last_name','phone','address','state','image')
    list_display_link = ('user','first_name','last_name')
    
    
    
admin.site.register(Profile, ProfileAdmin)


