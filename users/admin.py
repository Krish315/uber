from django.contrib import admin

# Register your models here.
from users.models import(Student)
admin.site.register(Student)
from users.models import(Order)
admin.site.register(Order)
