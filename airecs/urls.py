from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recs/', views.recs, name='recs'),
]
