from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from .models import ClanUO, ZivotnoDelo, Statut, Pravilnik, Kodeks, Istorijat, Faq
# Create your views here.


class ClanoviUOView(generic.ListView):
	model = ClanUO
	template_name = 'ukts/onama/clanovi_uo.html'
	# template_name = 'magazin_list.html'
	context_object_name = 'clanovi'
	# paginate_by = 4


	def get_queryset(self):
		return ClanUO.objects.order_by('-id')




class ZivotnoDeloView(generic.ListView):
    queryset = ZivotnoDelo.published.all()
    # queryset = get_object_or_404(ZivotnoDelo,  status='published')

    context_object_name = 'zivotno'
    # paginate_by = 3
    template_name = 'ukts/onama/zivotno_delo.html'



class StatutView(generic.ListView):
    queryset = Statut.published.all()
    # queryset = get_object_or_404(ZivotnoDelo,  status='published')

    context_object_name = 'statut'
    # paginate_by = 3
    template_name = 'ukts/onama/statut.html'


class PravilnikView(generic.ListView):
    queryset = Pravilnik.published.all()
    # queryset = get_object_or_404(ZivotnoDelo,  status='published')

    context_object_name = 'pravilnik'
    # paginate_by = 3
    template_name = 'ukts/onama/pravilnik.html'


class KodeksView(generic.ListView):
    queryset = Kodeks.published.all()
    # queryset = get_object_or_404(ZivotnoDelo,  status='published')

    context_object_name = 'kodeks'
    # paginate_by = 3
    template_name = 'ukts/onama/kodeks.html'


class IstorijatView(generic.ListView):
    queryset = Istorijat.published.all()
    # queryset = get_object_or_404(ZivotnoDelo,  status='published')

    context_object_name = 'istorijat'
    # paginate_by = 3
    template_name = 'ukts/onama/istorijat.html'



class KontaktView(generic.ListView):
    queryset = Istorijat.published.all()
    template_name = 'ukts/onama/kontakt.html'

class FaqView(generic.ListView):
    model = Faq
    # queryset = Faq.get_queryset()
    template_name = 'ukts/onama/faq.html'

    context_object_name = 'faqs'




# def ZivotnoDelo(request):
# #    posts = Post.published.all()
#     object_list = ZivotnoDelo.published.all()

#     context = {'zivotno': object_list}

#     return render(request, 'ukts/onama/zivotno_delo.html', context)