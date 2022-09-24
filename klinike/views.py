from django.contrib import messages 
from django.shortcuts import redirect, reverse, render
from django.urls import reverse_lazy
from django.views import generic
from .models import Klinike, TrenerskiDani, BCB, BCB_Promocija, BCB_Predavac, SlikeBCB, TD, SlikeTD

from .forms import PrijavaForm

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from ukts_website.settings import EMAIL_HOST_USER

from django.contrib import messages

# from urllib import urlopen, unquote
# from urlparse import parse_qs, urlparse


class KlinikaView(generic.ListView):
    model = Klinike
    template_name = 'ukts/klinike/klinike_bcb.html'
    # template_name = 'magazin_list.html'
    context_object_name = 'klinike'
    # paginate_by = 4

    # def get_context_data(self, **kwargs):
    # 		context = super(KlinikaView, self).get_context_data(**kwargs) # get the default context data
    # 		url_data = urlparse(Klinike.objects.values_list('link', flat = True)) # add extra field to the context
    # 		query = urlparse.parse_qs(url_data.query)
    # 		context['videoID'] = query["v"][0]
    # 		return context

    def get_queryset(self):
        return Klinike.objects.order_by('-godina')


class TrenerskiDaniView(generic.ListView):
    model = TrenerskiDani
    template_name = 'ukts/klinike/klinike_td.html'
    # template_name = 'magazin_list.html'
    context_object_name = 'klinike'
    # paginate_by = 4


    def get_queryset(self):
        return TrenerskiDani.objects.order_by('-godina')



def GalerijaBCBView(request):
    klinike = BCB.objects.all()
    slike = SlikeBCB.objects.all()
    context = {'klinike': klinike, 'slike': slike}
    return render(request, 'ukts/klinike/galerija_bcb.html', context)



def GalerijaTDView(request):
    trenerski_dani = TD.objects.all()
    slike = SlikeTD.objects.all()
    context = {'trenerski_dani': trenerski_dani, 'slike': slike}
    return render(request, 'ukts/klinike/galerija_td.html', context)



def PrijavaView(request):
    if request.method == "GET":
        form = PrijavaForm()
    else:
        form = PrijavaForm(request.POST)
        if form.is_valid():
            # subject = form.cleaned_data["subject"]
            # from_email = form.cleaned_data["from_email"]
            # message = form.cleaned_data['message']
            from_email = EMAIL_HOST_USER


            subject = "Aplikacija za BCB" 
            body = {
                'ime' : form.cleaned_data["ime"],
                'prezime' : form.cleaned_data["prezime"],
                'telefon' : str(form.cleaned_data["telefon"]),
                'email' : form.cleaned_data["email"],
            }
            message = "\n\n".join(body.values())

            # ime = form.cleaned_data["ime"]
            # prezime = form.cleaned_data["prezime"]
            # telefon = form.cleaned_data["telefon"]
            # email = form.cleaned_data["email"]
            # message = form.cleaned_data['message']

            try:
                send_mail(subject, message, from_email, ["admin@example.com"])
                messages.success(request, 'Thank you!', extra_tags='bcb')
                return redirect("klinike:prijava_bcb")
            except BadHeaderError:
                messages.error(request, 'Invalid form submission.')
                messages.error(request, form.errors)
                # return HttpResponse("Invalid header found.")
            # return redirect("klinike:success")
    return render(request, "ukts/klinike/aplication.html", {"form": form})

def SuccessPrijavaView(request):
    return HttpResponse("Success! Thank you for your message.")

