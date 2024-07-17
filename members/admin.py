from django.contrib import admin
from .models import Mymember

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date",)
  
admin.site.register(Mymember, MemberAdmin)