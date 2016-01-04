from django.shortcuts import render
from django.http import HttpResponse
from .forms import PatientForm

# Create your views here.

def index(request):
  form = PatientForm(request.POST or None)
  if form.is_valid():
    new_patient = form.save(commit=False)
    new_patient.save()
  context = {'form': form}
  template = 'dash/index.html'
  return render(request, template, context)

def summary(request):
  return render(request, "dash/summary.html")