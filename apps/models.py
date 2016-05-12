from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Users(models.Model):
    ID_Users = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=25)
    Last_Name = models.CharField(max_length=25)
    Age = models.DateField(default=timezone.now)
    SEX = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    Sex = models.CharField(max_length=1, choices=SEX)
    Mail = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    Phone = models.CharField(validators=[phone_regex], blank = True, max_length=15)

class Medic(models.Model):
    ID_Medic = models.AutoField(primary_key=True)
    ID_Users = models.ForeignKey(Users)
    Speciality = models.CharField(max_length=25)
    Prof_License = models.CharField(max_length=25)

class Patient(models.Model):
    ID_Patient = models.AutoField(primary_key=True)
    ID_Users = models.ForeignKey(Users)
    Marital_Status = models.CharField(max_length=25)
    Ocupation = models.CharField(max_length=25)

class Non_Pathological_History(models.Model):
    ID_Non_Pathological = models.AutoField(primary_key=True)
    ID_Users = models.ForeignKey(Users)
    Hypertension = models.BooleanField()
    Hypotension = models.BooleanField()
    Diabetes = models.BooleanField()
    Hepatitis = models.BooleanField()
    Tuberculosis = models.BooleanField()
    Complications = models.BooleanField()
    Trouble_Breathing = models.BooleanField()
    Alcohol = models.BooleanField()

class Pathological_History(models.Model):
    ID_Pathological = models.AutoField(primary_key=True)
    ID_Users = models.ForeignKey(Users)
    Actual_Threatment = models.BooleanField()
    Actual_Medicine = models.BooleanField()
    Allergies = models.BooleanField()
    Anestesic_Reaction = models.BooleanField()
    Hemorrhages = models.BooleanField()
    Complications = models.BooleanField()
    Angina_Pectoris = models.BooleanField()

class Teeths(models.Model):
    ID_Teeths = models.AutoField(primary_key=True)
    Number = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(85)])

class Appointment(models.Model):
    ID_Appointment = models.AutoField(primary_key=True)
    Date = models.DateField(default=timezone.now)
    ID_Medic = models.ForeignKey(Medic)
    ID_Patient = models.ForeignKey(Patient)

class Bill(models.Model):
    ID_Bill = models.AutoField(primary_key=True)
    ID_Appointment = models.ForeignKey(Appointment)
    Owes = models.DecimalField(max_digits=6, decimal_places=2)

class Treatments(models.Model):
    ID_Treatments = models.AutoField(primary_key=True)
    Description = models.TextField()
    Cost = models.DecimalField(max_digits=6, decimal_places=2)

class Treatments_Appointment(models.Model):
    ID_Treatments = models.ForeignKey(Treatments)
    ID_Appointment = models.ForeignKey(Appointment)
    ID_Teeths = models.ForeignKey(Teeths)

class Diagnostic(models.Model):
    ID_Diagnostic = models.AutoField(primary_key=True)
    Description = models.TextField()
    ID_Appointment = models.ForeignKey(Appointment)
