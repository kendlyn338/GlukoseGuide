from django.contrib import admin
from .models import Patient, Glucose

# Register your models here.
admin.site.register(Patient)
admin.site.register(Glucose)
