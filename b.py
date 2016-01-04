from dash.models import Patient, Group, Payment, Treatment
from django.db.models import Sum, Count, Avg, Q, Max
from itertools import chain
from operator import attrgetter
from copy import deepcopy
# stackoverflow: copy() will not work in the last case, you need deepcopy() whenever you have a reference inside the object

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

# merge_var = 'id'
l1 = [{'id':'1','name':'liad'}, {'id':'2','name':'lee'}]
l2 = [{'id':'1','age':'32'}, {'id':'2','age':'30'}]
l3 = [{'id':'1','age1':'321'}, {'id':'2','age1':'301'}]
l4 = [{'id':'1','age2':'322'}, {'id':'2','age2':'302'}]
L = [l1,l2,l3,l4]
merge_by_id = merger_by('id')
# merge_dicts_in_list(l1, l2, merge_var)
print "\n"
merge(l1,l2)
reduce(merge_by_id, L)
reduce(merger_by('id'), L)