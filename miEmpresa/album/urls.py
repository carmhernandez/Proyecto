from django.conf.urls import url
from album import views

urlpatterns = [
    url(r'^$', views.first_view, name='first_view'),
    #el name permite dspues tomar el valor desde un href
    url(r'^cargo/$', views.cargo, name='cargo-list'),
    #?P<cateogory_id>[0-9]+ es un parametro que se envia con una expresino regular cmo numero
    url(r'^cargo/(?P<cargo_id>[0-9]+)/detail/$', views.cargo_detail, name='cargo-detail'),	

    #views.PhotoListView.as_view() -> permite llamar la vista de forma automatica con el as_view a traves de la clase
    url(r'^trabajo/$', views.TrabajoListView.as_view(), name='trabajo-list'),
    #pk es la llave primaria
    url(r'^trabajo/(?P<pk>[0-9]+)/detail/$', views.TrabajoDetailView.as_view(), name='trabajo-detail'),	
	#conexion url
	url(r'^trabajo/(?P<pk>[0-9]+)/update/$', views.TrabajoUpdate.as_view(), name='trabajo-update'),
    #editar
    url(r'^cargo/(?P<pk>[0-9]+)/update/$', views.CargoUpdate.as_view(), name='cargo-update'),
	#eliminar url
	url(r'^trabajo/(?P<pk>[0-9]+)/delete/$', views.TrabajoDelete.as_view(), name='trabajo-delete'),
    #eliminar url category
    url(r'^cargo/(?P<pk>[0-9]+)/delete/$', views.CargoDelete.as_view(), name='cargo-delete'),	
    #create
    url(r'^trabajo/create/$', views.TrabajoCreate.as_view(), name='trabajo-create'),
    #create category
    url(r'^cargo/create/$', views.CargoCreate.as_view(), name='cargo-create'),

]	

