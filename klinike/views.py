from django.contrib import messages 
from django.shortcuts import redirect, reverse, render
from django.urls import reverse_lazy
from django.views import generic
from .models import Klinike, TrenerskiDani, BCB, SlikeBCB, TD, SlikeTD



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




# youtube_watchurl="https://www.youtube.com/watch?v=dP15zlyra3c"
# q = urlparse(youtube_watchurl).query
# print 'query : ', q

# qs = parse_qs(urlparse(youtube_watchurl).query)
# print 'parse_qs : ', qs



###--#-#-#-#-#-#-#-#-#-#-# REAL ONE !!!!!!! 
# class GalerijaBCBView(generic.ListView):
# 	model = Photo
# 	template_name = 'ukts/klinike/galerija_bcb.html'
# 	# template_name = 'magazin_list.html'
# 	context_object_name = 'fotos'
# 	# paginate_by = 4

# 	def get_queryset(self):
# 		return Photo.objects.order_by('-id')

# class GalerijaBCBView(generic.ListView):
# 	model = PictureBCB
# 	template_name = 'ukts/klinike/galerija_bcb.html'
# 	# template_name = 'magazin_list.html'
# 	context_object_name = 'fotos'
# 	# paginate_by = 4


# 	def get_queryset(self):
# 		return PictureBCB.objects.order_by('-id')




# class GalerijaTDView(generic.ListView):
# 	model = Photo
# 	template_name = 'ukts/klinike/galerija_td.html'
# 	# template_name = 'magazin_list.html'
# 	context_object_name = 'fotos'
# 	# paginate_by = 4


# 	def get_queryset(self):
# 		return Photo.objects.order_by('-id')




# class IstorijaBCBView(generic.ListView):
# 	model = Klinike
	
# 	extra_context={'bcb': model.objects.filter(tip="bcb")}

# 	template_name = 'ukts/klinike/istorija_bcb.html'
# 	# template_name = 'magazin_list.html'
# 	context_object_name = 'klinike'
# 	# paginate_by = 4



# class IstorijaTDView(generic.ListView):
# 	model = Klinike

# 	extra_context={'broj_td': Klinike.objects.filter(tip="td").count(), 'broj_td_predavanja': model.objects.filter(tip="td").count()*4}

# 	template_name = 'ukts/klinike/istorija_td.html'
# 	# template_name = 'magazin_list.html'
# 	context_object_name = 'klinike'
# 	# paginate_by = 4





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

