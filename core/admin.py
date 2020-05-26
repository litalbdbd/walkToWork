from django.contrib import admin

from .models import Employee, City, Region, Job

admin.site.register(Employee)
admin.site.register(City)
admin.site.register(Region)
admin.site.register(Job)

