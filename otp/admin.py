from django.contrib import admin
from otp.models import Reg

# Register your models here.
class RegAdmin(admin.ModelAdmin):
    list_display=['FirstName','LastName','UserName','Password','CPassword','Emailid','MobileNo']
admin.site.register(Reg,RegAdmin)