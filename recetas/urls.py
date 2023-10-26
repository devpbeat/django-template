from django.urls import path
from .views import RecetaDetalle, RecetaCrear, RecetaActualizar, RecetaEliminar, RecetaList

urlpatterns = [
    path('lista/', RecetaList.as_view(), name='receta_lista'),
    path('detalle/<int:pk>', RecetaDetalle.as_view(), name='receta_detalle'),
    path('crear/', RecetaCrear.as_view(), name='receta_crear'),
    path('actualizar/<int:pk>', RecetaActualizar.as_view(), name='receta_actualizar'),
    path('borrar/<int:pk>', RecetaEliminar.as_view(), name='receta_borrar'),
]