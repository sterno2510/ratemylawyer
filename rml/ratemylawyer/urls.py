from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('lawyers', views.lawyers, name='lawyers'),
    path('social', views.social, name='social'),
    path('reachout', views.reachout, name='reachout'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('edit', views.edit, name='edit'),
]
