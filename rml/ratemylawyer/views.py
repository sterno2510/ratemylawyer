from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from datetime import datetime

# Create your views here.

def lawyers(request):
     if request.method == 'GET':
          lawyer_list = Lawyer.objects.all()
     return render(request=request, template_name='rate/lawyers.html' )

def index(request):
     now = datetime.now()
     current_year = now.year
     return render(request, 'rate/index.html',)

def social(request):
     return render(request=request, template_name='rate/social.html')

def about(request):
     return render(request=request, template_name='rate/about.html')

def reachout(request):
     return render(request=request, template_name='rate/reachout.html')

def create(request):
     return render(request=request, template_name='rate/create.html')

def edit(request):
     return render(request=request, template_name='rate/edit.html')

