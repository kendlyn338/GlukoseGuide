from django.forms import ModelForm
from .models import Glucose, Profile

class GlucoseForm(ModelForm):
  class Meta:
    model = Glucose
    fields = ['date', 'meal', 'accucheck', 'carbohydrates', 'insulin']


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('user', 'physician', 'insulin_type', 'insulin_scale', 'phone_number', 'email')