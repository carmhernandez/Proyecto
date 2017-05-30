
from django.shortcuts import render
from django.http import HttpResponse
from album.models import Cargo, Trabajo
from django.views.generic import ListView, DetailView
from django.views.generic import UpdateView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy
# Create your views here.

class TrabajoUpdate(UpdateView):
	model=Trabajo
	fields='__all__'

class CargoUpdate(UpdateView):
	model=Cargo
	fields='__all__'

class TrabajoCreate(CreateView):
	model=Trabajo
	fields='__all__'

class CargoCreate(CreateView):
	model=Cargo
	fields='__all__'

class TrabajoDelete(DeleteView):
	model=Trabajo
	success_url=reverse_lazy('trabajo-list')

class CargoDelete(DeleteView):
	model=Cargo
	success_url=reverse_lazy('cargo-list')


#funcion que carga contenido html en la pagina
def first_view(request):
	return HttpResponse('<h1>Prueba vista</h1>')

#vista para las categorias
"""
permite crear las vistas para categoria

un objeto lista = modelo.objects.all() -> forma para django decirle que se haga un select * desde una tabla(modelo)
context= es un diccionario con las listas
se lo envia al template que se llama category dentro de album

"""
def cargo(request):
	cargo_list=Cargo.objects.all()
	context = {'object_list':cargo_list}
	return render(request, 'album/cargo.html', context);

"""
funccion que permite llamar los detalles de una categoria en especifico llamada por el id

recibe como parametro el identificador 
"""
def cargo_detail(request,cargo_id):
	cargo=Cargo.objects.get(id=cargo_id)
	context = {'object':cargo}
	return render(request, 'album/cargo_detail.html', context);


"""
funcion para las fotos
se crea con vista basada en clase

cuando se define una clase y lo que esta en parentesis es una herencia
"""
class TrabajoListView(ListView):
	"""doc string for PhotoListView"""
	model=Trabajo

class TrabajoDetailView(DetailView):
	model=Trabajo
