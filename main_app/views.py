from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Patient, User, Glucose
from .forms import GlucoseForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin







def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('patients_create')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


            
  
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def reference(request):
    return render(request, 'reference.html')


def patients_index(request):
    patients = Patient.objects.filter(user=request.user)
    return render(request, 'patients/index.html', { 'patients' : patients })


def patients_detail(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    glucose_form = GlucoseForm()
    return render(request, 'patients/detail.html', {
    'patient': patient, 
    'glucose_form' : glucose_form,
    })


def add_glucose(request, patient_id):
    form = GlucoseForm(request.POST)
    if form.is_valid():
        new_glucose = form.save(commit=False)
        new_glucose.patient_id = patient_id
        new_glucose.save()
    return redirect('patients_detail', patient_id=patient_id)


# update Glucose Form 
# class GlucoseUpdate(LoginRequiredMixin, UpdateView):
#     model = Glucose
#     fields = ('date', 'meal', 'accucheck', 'carbohydrates', 'insulin')

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)




class PatientCreate(LoginRequiredMixin, CreateView):
    model = Patient
    fields = ('name', 'month', 'day', 'year', 'phone_number', 'email', 'physician', 'insulin_type', 'insulin_scale')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
   


class PatientUpdate(LoginRequiredMixin, UpdateView):
    model = Patient
    fields = '__all__'


class PatientDelete(LoginRequiredMixin, DeleteView):
    model = Patient
    fields = '__all__'
    success_url = '/patients'





