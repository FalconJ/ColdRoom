from django import forms
from .models import SignUp, Datos
from django.utils import timezone
import datetime

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name', 'email']

class Fechas(forms.Form):

	CHOICES=[('pdf/temperaturaRep.html','Temperatura'),
         ('pdf/humedadRep.html','Humedad'),
         ('pdf/corrienteRep.html', 'Corriente')]

	Fecha_Inicial = forms.DateField(initial=datetime.date.today)
	Fecha_Final = forms.DateField(initial=datetime.date.today)
	opcion = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
