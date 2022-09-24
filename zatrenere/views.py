from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import Planeri, Lekarski, Uplatnice, Aplikacija
from .forms import AplikacijaForm

from ukts_website.settings import EMAIL_HOST_USER
from django.contrib import messages


class PlaneriView(generic.ListView):
	model = Planeri
	template_name = 'ukts/zatrenere/planeri.html'
	# template_name = 'magazin_list.html'
	context_object_name = 'planeri'
	# paginate_by = 4


	def get_queryset(self):
		return Planeri.objects.order_by('-id')


class LekarskiView(generic.ListView):
	model = Lekarski
	template_name = 'ukts/zatrenere/lekarski.html'
	# template_name = 'magazin_list.html'
	context_object_name = 'lekarski'
	# paginate_by = 4


	def get_queryset(self):
		return Lekarski.objects.order_by('-id')


class UplatniceView(generic.ListView):
	model = Uplatnice
	template_name = 'ukts/zatrenere/uplatnice.html'
	# template_name = 'magazin_list.html'
	context_object_name = 'uplatnice'
	# paginate_by = 4


	def get_queryset(self):
		return Uplatnice.objects.order_by('-id')


# def AplikacijaView(request):
#     if request.method == 'GET':
#         form = AplikacijaForm()
#         print("in GET")
#     elif request.method == 'POST':
#         form = AplikacijaForm(request.POST, request.FILES)
#         print("in post")
#         if form.is_valid():
			
#             subject = form.cleaned_data['prezime']
#             # from_email = form.cleaned_data['from_email']
#             body = {
# 				'ime': form.cleaned_data['ime'], 
# 				'prezime': form.cleaned_data['prezime'], 
# 				# 'email': form.cleaned_data['email_address'], 
# 				# 'message':form.cleaned_data['message'], 
# 			}
#             message = "\n".join(body.values())

#             print("is valid")

#             try:
#                 email = EmailMessage(subject, message, EMAIL_HOST_USER, ['stevanv@gmx.de'])
#                 email.content_subtype = 'html'

#                 diploma = form.cleaned_data['diploma']
#                 email.attach(diploma.name, diploma.read(), diploma.content_type )

#                 email.send()
#                 # send_mail(subject, message, from_email, ['stevanv@gmx.de'])
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')

#             return HttpResponse("Sent")
#             # return redirect('success')
#     return render(request, "ukts/zatrenere/aplikacija.html", {'form': form})


def AplikacijaView(request):
    if request.method == "GET":
        form = AplikacijaForm()
    else:
        # print("in post")
        form = AplikacijaForm(request.POST, request.FILES)
        if form.is_valid():

            from_email = EMAIL_HOST_USER

            subject = "Aplikacija za Trenere "  + str(form.cleaned_data["prezime"])

            ime = form.cleaned_data["ime"]
            prezime = form.cleaned_data["prezime"]
            telefon = str(form.cleaned_data["telefon"])
            email = form.cleaned_data["email"]
            adresa = form.cleaned_data["adresa"]
            grad = form.cleaned_data["grad"]
            opstina = form.cleaned_data["opstina"]
            broj_opstine = form.cleaned_data["broj_opstine"]
            drzava = form.cleaned_data["drzava"]
            broj_licence = form.cleaned_data["broj_licence"]
            boja_licence = form.cleaned_data["boja_licence"]
            zvanje_licenca = form.cleaned_data["zvanje_licenca"]
            diploma_broj = form.cleaned_data["diploma_broj"]
            fakultet = form.cleaned_data["fakultet"]


            # body = {
            #     'ime' : ("Ime:  " + form.cleaned_data["ime"]),
            #     'prezime' : ("Prezime:  " + form.cleaned_data["prezime"]),
            #     'telefon' : ("Telefon:  " + str(form.cleaned_data["telefon"])),
            #     'email' : ("Email:  " + form.cleaned_data["email"]),
            #     'adresa' : ("Adresa:  " + form.cleaned_data["adresa"]),
            #     'grad' : ("Grad:  " + form.cleaned_data["grad"]),
            #     'opstina' : ("Opstina:  " + form.cleaned_data["opstina"]),
            #     'broj_opstine' : ("Broj opstine:  " + form.cleaned_data["broj_opstine"]),
            #     'drzava' : ("Drzava:  " + form.cleaned_data["drzava"]),
            #     'broj_licence' : ("Broj licence:  " + form.cleaned_data["broj_licence"]),
            #     'boja_licence' : ("Boja licence:  " + form.cleaned_data["boja_licence"]),
            #     'zvanje_licenca' : ("Zvanje licence:  " + form.cleaned_data["zvanje_licenca"]),
            #     'diploma_broj' : ("Broj diplome, datum i mesto izdavanja:  " + form.cleaned_data["diploma_broj"]),
            #     'fakultet' : ("Fakultet:  " + form.cleaned_data["fakultet"]),
            # }
            # message = "\n\n".join(body.values())


            email_body = """\
                <html>
                <head></head>
                <body>
                    <h1>Aplikacija preko ukts websajta:</h1>
                    <h3>Ime i prezime:</h3>
                    <p>%s %s</p>
                    </br>
                    <h3>Telefon:</h3>
                    <p>%s</p>
                    </br>
                    <h3>Email:</h3>
                    <p>%s</p>
                    </br>
                    <h3>Adresa:</h3>
                    <p>%s</p>
                    </br>
                    <h3>Grad:</h3>
                    <p>%s</p>
                    </br>
                    <h3>Opstina:</h3>
                    <p>%s</p>
                    </br>
                    <h3>Broj opstine:</h3>
                    <p>%s</p>
                    </br>
                    <h3>Drzava:</h3>
                    <p>%s</p>
                    </br>
                    <h3>Broj licence:</h3>
                    <p>%s</p>
                    </br>
                    <h3>Boja licence:</h3>
                    <p>%s</p>
                    </br>
                    <h3>Zvanje licence:</h3>
                    <p>%s</p>
                    </br>
                    <h3>Diploma datum, mesto izdavanja i broj diplome, kao i akademsko zvanje:</h3>
                    <p>%s</p>
                    </br>
                    <h3>Fakultet:</h3>
                    <p>%s</p>
                    </br>
                </body>
                </html>
                """ % (ime, prezime, telefon, email, adresa, grad, opstina, broj_opstine, drzava, broj_licence, boja_licence, zvanje_licenca, diploma_broj, fakultet)


            try:
                # print("in try")
                email = EmailMessage(subject, email_body, EMAIL_HOST_USER, ['stevanv@gmx.de'])
                email.content_subtype = 'html'

                if form.cleaned_data['diploma']:
                    # print("in diploma")
                    file = form.cleaned_data['diploma']
                    if hasattr(file, 'path'):
                        email.attach_file(file.path)
                    else:
                        email.attach(file.name, file.read())

                if form.cleaned_data['slika']:
                    # print("in diploma")
                    file = form.cleaned_data['slika']
                    if hasattr(file, 'path'):
                        email.attach_file(file.path)
                    else:
                        email.attach(file.name, file.read())

                email.send()

            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            messages.success(request, 'Hvala', extra_tags='aplikacija')
            return redirect("zatrenere:aplikacija")
    return render(request, "ukts/zatrenere/aplikacija.html", {"form": form})

def SuccessAplikacijaView(request):
    return HttpResponse("Success! Thank you for your message.")