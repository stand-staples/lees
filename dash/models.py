from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Patient(models.Model):
  GENDERS = (('female','Female'),
             ('male','Male'),
             ('unknown','Unknown'),)
#  TRAINEE = (('yes','Trainee'),('no','Patient'))
  patient_name = models.CharField(
    max_length=200, 
    unique = True)
  year_of_birth = models.IntegerField()
  gender = models.CharField(
    max_length=20,
    choices = GENDERS)
  phone_number = models.CharField(max_length=200)
  default_price = models.IntegerField()
  email = models.EmailField()
  address = models.CharField(max_length=200)
  how_arrived = models.CharField(max_length=100)
  comments = models.CharField(max_length=200)
  is_trainee = models.CharField(max_length=20)
  is_archived = models.BooleanField(default=False)
  is_deleted = models.BooleanField(default=False)
  def __unicode__(self):
    return u'%s' %self.patient_name
  
class Group(models.Model):
    patient = models.ForeignKey(
      Patient, 
      on_delete=models.CASCADE
#     limit_choices_to={'is_deleted': False,'is_archived': False, 'is_trainee': True},
    )
    group_date = models.DateField()
    group_hour = models.TimeField()
    price = models.IntegerField()
    comments = models.CharField(max_length=200)

class Payment(models.Model):
  P_TYPES = (('cheque','Cheque'),
             ('cash','Cash'),
             ('transfer','Transfer'),
             ('other','Other'),)
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  payment_date = models.DateField()
  comments = models.CharField(max_length=200)
  amount = models.IntegerField()
  receipt_num = models.IntegerField()
  payment_type = models.CharField(
    max_length=20,
    choices = P_TYPES
  )
  is_deleted = models.BooleanField(default=False)
    
class Treatment(models.Model):
  patient = models.ForeignKey(
    Patient,
    on_delete=models.CASCADE
#     limit_choices_to={'is_deleted': False,'is_archived': False, 'is_trainee': True},
  )
  treatment_date = models.DateField()
  main_concern = models.CharField(max_length=200)
  what_we_did = models.CharField(max_length=200)
  home_work =models.CharField(max_length=200)
  comments = models.CharField(max_length=200)
  price = models.IntegerField()
  is_deleted = models.BooleanField(default=False)
  