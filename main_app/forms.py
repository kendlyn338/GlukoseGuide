from django.forms import ModelForm
from .models import Glucose

class GlucoseForm(ModelForm):
  class Meta:
    model = Glucose
    fields = ['date', 'meal', 'accucheck', 'insulin']