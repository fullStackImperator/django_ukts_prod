import csv
import datetime
import imp
import re

from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import TreneriForm
from .models import Trener

# Create your views here.


def treneri_list(request):
    treneri = Trener.objects.all()
    context = {'treneri_list' : treneri}
    return render(request, "treneri/treneri_list.html", context)

def treneri_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = TreneriForm()
        else:
            trener = Trener.objects.get(pk=id)
            form = TreneriForm(instance=trener)
        context = {'form' : form}
        return render(request, "treneri/treneri_form.html", context)
    else:
        if id == 0:
            form = TreneriForm(request.POST)
        else:
            trener = Trener.objects.get(pk=id)
            form = TreneriForm(request.POST, instance=trener)

        if form.is_valid():
            form.save()
        return redirect('/treneri/list')

def treneri_delete(request, id):
    trener = Trener.objects.get(pk=id)
    if request.method =="POST":
        trener.delete()
        return redirect('/treneri/list')
    
    return redirect('/')


def export_csv(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename=Treneri_'+ str(datetime.datetime.now().date()) + '.csv'

    writer = csv.writer(response)
    writer.writerow(['Ime', 'Licenca', 'Klub', 'Email', 'Telefon'])

    treneri = Trener.objects.all()

    for trener in treneri:
        writer.writerow([trener.ime, trener.licenca, trener.klub, trener.email, trener.telefon])

    return response