from django.shortcuts import redirect, render
from django.views import generic
from .models import Knjige
# Create your views here.


class KnjigeView(generic.ListView):
	model = Knjige
	template_name = 'ukts/edukacija/knjige_list.html'
	# template_name = 'magazin_list.html'
	context_object_name = 'knjige'
	# paginate_by = 4


	def get_queryset(self):
		return Knjige.objects.order_by('-id')