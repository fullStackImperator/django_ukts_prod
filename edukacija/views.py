from django.shortcuts import redirect, render
from django.views import generic
from .models import Knjige, FibaAssist, StrucneTeme, Linkovi, LinkoviPDF
# Create your views here.


class KnjigeView(generic.ListView):
	model = Knjige
	template_name = 'ukts/edukacija/knjige_list.html'
	# template_name = 'magazin_list.html'
	context_object_name = 'knjige'
	# paginate_by = 4


	def get_queryset(self):
		return Knjige.objects.order_by('id')



class FibaAssistView(generic.ListView):
	model = FibaAssist
	template_name = 'ukts/edukacija/fiba_assist.html'
	# template_name = 'magazin_list.html'
	context_object_name = 'assists'
	# paginate_by = 4


	def get_queryset(self):
		return FibaAssist.objects.order_by('id')


class StrucneTemeView(generic.ListView):
	model = StrucneTeme
	template_name = 'ukts/edukacija/strucne_teme.html'
	# template_name = 'magazin_list.html'
	context_object_name = 'teme'
	# paginate_by = 4


	def get_queryset(self):
		return StrucneTeme.objects.order_by('id')


# class LinkoviView(generic.ListView):
# 	model = Linkovi
# 	template_name = 'ukts/edukacija/linkovi.html'
# 	# template_name = 'magazin_list.html'
# 	context_object_name = 'linkovi'
# 	# paginate_by = 4


# 	def get_queryset(self):
# 		return Linkovi.objects.order_by('id')

def linkovi(request):
       linkovi = Linkovi.objects.all()
       linkoviPDF = LinkoviPDF.objects.all()

       context = {
              'linkovi': linkovi,
              'linkoviPDF': linkoviPDF
       }
       return render(request, 'ukts/edukacija/linkovi.html', context)