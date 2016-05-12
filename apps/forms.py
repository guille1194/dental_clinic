from django import forms
from django.forms import ModelForm
from .models import Users, Medic, Patient, Non_Pathological_History, Pathological_History, Teeths, Appointment, Bill, Treatments, Treatments_Appointment, Diagnostic
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):

	class Meta:
		model = Users
		fields = '__all__'
