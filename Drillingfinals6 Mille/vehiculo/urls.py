from django.urls import path
#from . import views
from .views import IndexPageView, registro_view, login_view, logout_view, \
    add_view, registrarauto_view, eliminarauto_view, edicionauto_view,\
    editarauto_view, listar_view, listarjs_view, list_autos_view

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('index/', IndexPageView.as_view(), name='index'),
    path('registro/', registro_view, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('add/', add_view, name='add'),
    path('registrarauto/', registrarauto_view, name='registrarauto'),
    path('add/eliminarauto/<id>', eliminarauto_view, name='eliminarauto'),
    path('add/edicionauto/<int:id>/', edicionauto_view, name='edicionauto'),
    path('add/editarauto/<int:id>/', editarauto_view, name='editarauto'),
    path('listar/', listar_view, name='listar'),
    path('listarjs/', listarjs_view, name='listarjs'),
    path('list_autos/', list_autos_view, name='list_autos'),
]

