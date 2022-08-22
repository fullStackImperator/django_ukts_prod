import csv
import datetime
import imp
import json
import re

import xlwt
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

from .forms import TreneriForm
from .models import Trener
from klinike.models import SlikeBCB, BCB, TD, SlikeTD

from django.views.generic import ListView
import json
from django.http import JsonResponse

from django.core import serializers

# Create your views here.

# @login_required
def treneri_list(request):
	treneri = Trener.objects.all()
	
	# paginator = Paginator(treneri, 2)
	# page_number=request.GET.get('page')
	# page_obj=Paginator.get_page(paginator, page_number)

	context = {'treneri_list' : treneri} #, 'page_obj':page_obj}
	return render(request, "treneri/treneri_list.html", context)

# @login_required
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
			form = TreneriForm(request.POST, request.FILES)
		else:
			trener = Trener.objects.get(pk=id)
			form = TreneriForm(request.POST, request.FILES, instance=trener)

		if form.is_valid():
			form.save()
		return redirect('/treneri/list')

# @login_required
def treneri_delete(request, id):
	trener = Trener.objects.get(pk=id)
	if request.method =="POST":
		trener.delete()
		return redirect('/treneri/list')
	
	return redirect('/')




def uploadBCBView(request):
	klinike = BCB.objects.all()
	
	if request.method == 'POST':
		data = request.POST
		slike = request.FILES.getlist('slike')
		# images = request.FILES.getlist('images')

		if data['godina'] != 'none':
			godina = BCB.objects.get(id=data['godina'])
		elif data['godina_nova'] != '':
			godina, created = BCB.objects.get_or_create(godina=data['godina_nova'])
		else:
			godina = None

		for slika in slike:
			slika = SlikeBCB.objects.create(
					klinika=godina,
					# godina=request.POST.get('godina'),
					slika=slika,
				)

		return redirect('/treneri/list')

		# print('data:', data)
		# print('slika:', slika)

	context = {'klinike': klinike}
	return render(request,  "treneri/foto_upload_bcb.html", context)



def uploadTDView(request):
	trenerski_dani = TD.objects.all()
	
	if request.method == 'POST':
		data = request.POST
		slike = request.FILES.getlist('slike')
		# images = request.FILES.getlist('images')

		if data['godina'] != 'none':
			godina = TD.objects.get(id=data['godina'])
		elif data['godina_nova'] != '':
			godina, created = TD.objects.get_or_create(godina=data['godina_nova'])
		else:
			godina = None

		for slika in slike:
			slika = SlikeTD.objects.create(
					trenerski_dan=godina,
					# godina=request.POST.get('godina'),
					slika=slika,
				)

		return redirect('/treneri/list')

		# print('data:', data)
		# print('slika:', slika)

	context = {'trenerski_dani': trenerski_dani}
	return render(request,  "treneri/foto_upload_td.html", context)






@login_required
def export_csv(request):

	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition']='attachment; filename=Treneri_'+ str(datetime.datetime.now().date()) + '.csv'

	writer = csv.writer(response)
	writer.writerow(['Ime', 'Licenca', 'Klub', 'Email', 'Telefon', 'Region', 'Datum rodjenja'])

	treneri = Trener.objects.all()

	for trener in treneri:
		writer.writerow([trener.ime, trener.licenca, trener.klub, trener.email, trener.telefon, trener.region, trener.datum_rodjenja])

	return response

@login_required
def export_excel(request):

	response = HttpResponse(content_type='application/ms-excel')
	response['Content-Disposition']='attachment; filename=Treneri_'+ str(datetime.datetime.now().date()) + '.xls'

	wb = xlwt.Workbook(encoding='utf-8')
	ws = wb.add_sheet('Treneri')
	row_num = 0
	font_style = xlwt.XFStyle()
	font_style.font.bold = True

	columns = ['Ime', 'Licenca', 'Klub', 'Email', 'Telefon', 'Region', 'Datum rodjenja']

	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)

	font_style = xlwt.XFStyle()

	rows=Trener.objects.all().values_list('ime', 'licenca', 'klub', 'email', 'telefon', 'region', 'datum_rodjenja')

	for row in rows:
		row_num+=1

		for col_num in range(len(row)):
			ws.write(row_num, col_num, row[col_num], font_style)

	wb.save(response)

	return response

@login_required
def export_pdf(request):
	pass




def is_ajax(request):
	return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def main_search_view(request):

	return render(request, 'ukts/licenca/search_trener.html', {})

def trener_detail_view(request, pk):
	obj = get_object_or_404(Trener, pk=pk)
	return render(request, 'ukts/licenca/trener_detail.html', {'obj': obj})
	# post_url+'#'+str(reply.id

def search_results(request):
	if is_ajax(request=request):
		res = None
		trener = request.POST.get('trener')
		# print(trener)
		qs = Trener.objects.filter(ime__icontains=trener)
		# print(qs)
		if len(qs) > 0 and len(trener) > 0:
			data = []
			for pos in qs:
				item = {
					'pk': pos.pk, 
					'ime': pos.ime,
					'licenca': pos.licenca,
					'slika': str(pos.slika.url),
					'slika_resize': str(pos.slika_resize.url),
				}
				data.append(item)
			res = data
		else:
			res = "Nema trenera sa tim imenom"

		return JsonResponse({'data': res})
	return JsonResponse({})









# class TrenerInfoView(ListView):
#     model = Trener
#     template_name = 'ukts/licenca/search_trener.html'

#     def get_cotext_data(self, **kwargs):
#         context = super(self).get_context_data(**kwargs)
		
#         treneri_list= Trener.objects.values()
#         # context["qs_json"] = json.dumps( list(Trener.objects.all().values()) )
#         context['qs_json'] = serializers.serialize('json', treneri_list, fields=('ime', 'licenca'))
		
#         # print ("TEST:")
#         # print (context['qs_json'])
#         #return JsonResponse(context, safe=False)
#         return context