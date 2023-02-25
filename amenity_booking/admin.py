from django.contrib import admin
from .models import *

# Register your models here.

class master_table_admin(admin.ModelAdmin):
  list_display = ('apt_no','first_name','last_name','phone')
admin.site.register(master,master_table_admin)

admin.site.register(signup_table)

class contact_table_admin(admin.ModelAdmin):
  list_display = ('name','email','message')
admin.site.register(contact_table, contact_table_admin)

admin.site.register(booking_table)
admin.site.register(amenity_type)
admin.site.register(amenity_slots)
admin.site.register(amenity_timings)
admin.site.register(uidtable)
admin.site.register(filled)
admin.site.register(amenity_maintenance)



