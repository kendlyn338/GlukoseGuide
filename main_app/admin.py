from django.contrib import admin
from django.contrib.auth.models import User



from .models import Patient, Glucose, Profile





# Register your models here.
admin.site.register(Patient)
admin.site.register(Glucose)
admin.site.register(Profile)
