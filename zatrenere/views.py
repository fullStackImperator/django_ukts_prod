from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import Planeri, Lekarski, Uplatnice, Aplikacija
from .forms import AplikacijaForm

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


def AplikacijaView(request):
    if request.method == 'GET':
        form = AplikacijaForm()
    else:
        form = AplikacijaForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['stevanv@gmx.de'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "ukts/zatrenere/aplikacija.html", {'form': form})