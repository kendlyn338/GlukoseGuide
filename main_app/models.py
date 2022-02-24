from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User




MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
    ('HS', 'Bedtime'),
    ('PRN', 'PRN if Needed')
)



class Patient(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    month = models.CharField(max_length=20)
    day = models.IntegerField()
    year = models.IntegerField()
    phone_number = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    physician = models.CharField(max_length=100)
    insulin_type = models.CharField(max_length=50)
    insulin_scale = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('patients_detail', kwargs={'patient_id': self.id})

    def checked_today(self):
        return self.glucose_set.filter(date=date.today()).count() >= len(MEALS)

class Glucose(models.Model):
    date = models.DateField('glucose date')
    meal = models.CharField(max_length=5, choices=MEALS, default=MEALS[0][0])
    accucheck = models.IntegerField()
    carbohydrates = models.IntegerField()
    insulin = models.IntegerField()
    
    
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        ordering = ['-date']

    def get_absolute_url(self):
        return reverse('patients_detail', kwargs={'patient_id': self.id})




    


