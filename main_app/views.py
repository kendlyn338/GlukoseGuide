from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Patient
from .forms import GlucoseForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def patients_index(request):
    patients = Patient.objects.all()
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


class PatientCreate(CreateView):
    model = Patient
    fields = '__all__'
    success_url = '/patients/'

class PatientUpdate(UpdateView):
    model = Patient
    fields = '__all__'

class PatientDelete(DeleteView):
    model = Patient
    fields = '__all__'
    success_url = '/patients'
    