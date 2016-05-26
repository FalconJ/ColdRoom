from django.conf.urls import url

from . import views

app_name = 'graficas'

urlpatterns = [
	url(r'^$', views.ReportesView.as_view(), name="index"),
	url(r'^reporte/$', views.ReporteView.as_view(), name='reporte'),
]