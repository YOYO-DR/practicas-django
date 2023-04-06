from django.shortcuts import render,redirect
from .forms import VotarForm
from .models import *

def index(request):
    context = {
        'titulo':'Principal'
    }
    return render(request, 'index.html',context)

def votacion(request):
  if request.method == 'GET':
    context ={
     'titulo':'Votación',
     'form':VotarForm
  }
    return render(request, 'votar.html',context)
  else:
    form = VotarForm(request.POST)
    if form.is_valid():
        try:
          form.save()
          return redirect('index')
        except Exception as e:
          context ={
     'titulo':'Votación',
     'form':VotarForm,
     'error':str(e)
  }
          return render(request, 'votar.html',context)
    else:
      context ={
     'titulo':'Votación',
     'form':VotarForm(data=request.POST),
     'error':'Ya hay un usuario con ese n° de cedula'
  }
      return render(request, 'votar.html',context)

def votaciones(request):
   context = {
      'titulo':'Votaciones',
      'votaciones':Votacion.objects.all()
   }
   return render(request, 'votaciones.html',context)