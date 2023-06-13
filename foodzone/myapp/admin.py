from django.contrib import admin
from myapp.models import contact,profile

# Register your models here.
admin.site.site_header = "Foodzone | Admin"
class contactadmin(admin.ModelAdmin):
    list_display= ['id','name','email','subject','added_on','is_approved']
admin.site.register(contact,contactadmin)


#To show table in the dashboard backecnd we have to write this:
admin.site.register(profile)


