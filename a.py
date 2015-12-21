from dash.models import Patient, Group, Payment, Treatment
from django.db.models import Sum

Patient.objects.values('patient_name').annotate(p = Sum('treatment__price'))