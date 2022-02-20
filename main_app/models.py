from django.db import models
from django.urls import reverse


MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
    ('HS', 'Bedtime')
)

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=100)
    month = models.CharField(max_length=20)
    day = models.IntegerField()
    year = models.IntegerField()
    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('patients_detail', kwargs={'patient_id': self.id})

class Glucose(models.Model):
    date = models.DateField('glucose date')
    meal = models.CharField(max_length=2, choices=MEALS, default=MEALS[0][0])
    accucheck = models.CharField(max_length=5)
    insulin = models.CharField(max_length=5)
    
    
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        ordering = ['-date']
