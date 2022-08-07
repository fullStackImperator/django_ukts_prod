from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from .models import Files


class FilesView(generic.ListView):
	model = Files
	template_name = 'ukts/magazin/magazin_detail.html'
	# template_name = 'magazin_list.html'
	context_object_name = 'files'
	# paginate_by = 4


	def get_queryset(self):
		return Files.objects.order_by('-id')



class IstorijaMagazinView(generic.ListView):
	model = Files
	template_name = 'ukts/magazin/magazin_istorija.html'
	# template_name = 'magazin_list.html'
	context_object_name = 'files'
	# paginate_by = 4


	def get_queryset(self):
		return Files.objects.order_by('-id')


# def magazin_istorija(request):
#     # treneri = Trener.objects.all()
    
#     # paginator = Paginator(treneri, 2)
#     # page_number=request.GET.get('page')
#     # page_obj=Paginator.get_page(paginator, page_number)

#     # context = {'treneri_list' : treneri} #, 'page_obj':page_obj}
#     return render(request, "ukts/magazin/magazin_istorija.html") #, context)