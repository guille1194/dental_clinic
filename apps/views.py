from django.shortcuts import render, redirect
from .models import Users, Medic, Patient, Non_Pathological_History, Pathological_History, Teeths, Appointment, Bill, Treatments, Treatments_Appointment, Diagnostic
from django.core.urlresolvers import reverse_lazy
from .forms import UserForm
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.
def index_view(request):
    return render(request, 'home/index_view.html')

def add_user(request):
    for x in range(0, 1000):
        us = Users()
        us.Name = str(x)
        us.Last_Name = str(x)
        us.Age = str(x)
        us.Sex = str(x)
        us.Mail = str(x)
        us.Phone = str(x)
        try:
            us.save()
        except:
            print ('listo')
            return redirect("index_view")
