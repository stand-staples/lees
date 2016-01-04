from dash.models import Patient, Group, Payment, Treatment
from django.db.models import Sum, Count, Avg, Q, Max
from itertools import chain
from operator import attrgetter

a = Patient.objects.values('patient_name').annotate(p2 = Sum('treatment__price'), p3 = Count('treatment__price'), max_d = Max('treatment__treatment_date'))
b = Patient.objects.values('patient_name').annotate(p = Sum('group__price'))
c = Patient.objects.values('patient_name').annotate(payment = Sum('payment__amount'), payment_cnt = Count('payment__amount'))

d = Patient.objects.values('patient_name')\
.annotate(payment = Sum('payment__amount'), payment_cnt = Count('payment__amount'))\
.annotate(tr_pr = Sum('treatment__price'), tr_cnt = Count('treatment__price'), max_tr_d = Max('treatment__treatment_date'))
#.annotate(gr_pr = Sum('group__price'),gr_cnt = Count('group__price'))

# Group.objects.values('price').all()

print '\n'
print a
print b
print c

print '\n'
print d



# result_list = list()
# print sorted(chain(a, b), key=attrgetter('patient_name'))
# res_list = chain(a,b)
# for element in res_list:
#   print element