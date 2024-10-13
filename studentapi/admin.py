from django.contrib import admin

from studentapi.models import Students


@admin.register(Students)
# Register your models here.
class Studentadmin(admin.ModelAdmin):
    list_display=['id','name','age','city']
