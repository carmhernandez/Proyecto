from django.db import models
from django.core.urlresolvers import reverse
class Cargo(models.Model):
    """ Categorias para clasificar las fotos """
    name = models.CharField(max_length=50)
    def __str__(self):             
        return self.name
    def get_absolute_url(self):
    	return reverse('cargo-list')

class Trabajo(models.Model):
	"""Fotos del album"""
	Cargo=models.ForeignKey(Cargo,null=True,blank=True)
	nombre=models.CharField(max_length=50,default='No title')
	foto=models.ImageField(upload_to='photos/')
	pub_date=models.DateField(auto_now_add=True)
	
	def get_absolute_url(self):
		return reverse('trabajo-list')
	def __str__(self):
		return self.title


class Estudiante(models.Model):
	"""estudiantes"""
	email=models.EmailField(max_length=50)
	nombres=models.CharField(max_length=100,blank=True)
	apellidos=models.CharField(max_length=100,blank=True)
	direccion=models.CharField(max_length=200,blank=True)
	fecha_nac=models.DateField(auto_now_add=False)
	observaciones=models.TextField()
	def __str__(self):
		return self.nombres+" "+self.apellidos