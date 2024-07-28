from django.urls import path
from . import views

app_name = 'patients'

urlpatterns = [
    path('all_patients/', views.listPatients, name='listPatients'),# <slug:group_slug>/
    path('patietn/', views.patient, name='patient'), #patient/<slug:client_slug>/
]