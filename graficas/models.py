from django.db import models

class SignUp(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length=120, blank=False, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.email


class Datos(models.Model):
	temperatura = models.FloatField()
	humedad = models.FloatField()
	corriente = models.FloatField()
	fecha_registro = models.DateTimeField(auto_now_add=True, auto_now=False)


class Persona(models.Model):
	nombre = models.CharField(max_length=120, blank=False, null=True)


