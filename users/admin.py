from django.contrib import admin

from users.models import Student

# Register your models here.


# admin.site.register(Student)

@admin.register(Student)

class StudentAdmin(admin.ModelAdmin):
    list_display=('name','email','age')
    search_fields = ['name','age','email']
    list_filter=['name','age']
    