from dash.models import Patient, Group, Payment, Treatment
from django.db.models import Sum, Count, Avg, Q, Max
from itertools import chain
from operator import attrgetter
from copy import deepcopy


def merge_list_of_dictionaries_by_var(merge_var):
  def merge_lists(l1, l2):
    d1 = {dic[merge_var]:dic for dic in l1}
    d2 = {dic[merge_var]:dic for dic in l2}
    keys = list(d1.viewkeys() & d2.viewkeys())
    # cannot be replaced by d1.copy !
    x = deepcopy(d1) 
    for key in keys:
      x[key].update(d2[key])
    return list(x.values())
  return merge_lists

a = Patient.objects.values('patient_name')\
    .annotate(p2 = Sum('treatment__price'), p3 = Count('treatment__price'), max_d = Max('treatment__treatment_date'))
b = Patient.objects.values('patient_name')\
    .annotate(p = Sum('group__price'))
c = Patient.objects.values('patient_name')\
    .annotate(payment = Sum('payment__amount'), payment_cnt = Count('payment__amount'))

L = [a,b,c]
reduce(merge_list_of_dictionaries_by_var('patient_name'), L)


