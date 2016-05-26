import os
import datetime

from django.conf import settings
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

import arrow
#from django_xhtml2pdf.utils import generate_pdf

from .models import Datos
from .forms import SignUpForm, Fechas

#Base class
class PdfResponseMixin(object, ):
    def write_pdf(self, file_object, ):
        context = self.get_context_data()
        template = self.get_template_names()[0]
        generate_pdf(template, file_object=file_object, context=context)

    def render_to_response(self, context, **response_kwargs):
        resp = HttpResponse(content_type='application/pdf')
        self.write_pdf(resp)
        return resp

# Create your views here.
class HomePageView(TemplateView):
	template_name = 'home.html'

class ReportesView(FormView):
	form_class = Fechas
	template_name = 'reportes.html'

	@method_decorator(login_required)
	def get(self, request, *args, **kwargs):
		form = self.form_class(initial=self.initial)
		return render(request, self.template_name, {'form': form})


class TempPdfListView(ListView):
	context_object_name = 'fechas'
	model = Datos
	template_name = 'pdf/temp.html'

class ReporteView(TemplateView):
	def post(self, request, *args, **kwargs):
		form = Fechas(request.POST)
		template_name = request.POST.get('opcion')

		if "temperatura" in template_name:
			opcion = 'temperatura'
		elif "humedad" in template_name:
			opcion = 'humedad'
		elif "corriente" in template_name:
			opcion = 'corriente'

		start = request.POST.get('Fecha_Inicial')
		end = request.POST.get('Fecha_Final')

		data = list(Datos.objects.values_list(opcion, flat=True).filter(fecha_registro__range=(start, end)).order_by("fecha_registro"))
		fechas = list(Datos.objects.values_list("fecha_registro", flat=True).filter(fecha_registro__range=(start, end)).order_by("fecha_registro"))

		return render(request, template_name, {'form':form, 'data':data, 'length':len(data), 'zip':zip(data, fechas)})