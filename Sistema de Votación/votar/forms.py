from django import forms
from .models import Votacion,Enterado

class VotarForm(forms.ModelForm):
  class Meta:
    model = Votacion
    fields = '__all__'
    exclude = ['fecha']
    OPCIONES=[]
    for i in Enterado.objects.all():
      opcion=(i.id,i.nombre)
      OPCIONES.append(opcion)

    widgets = {
      #para convertirlo en radio buttons, y las opciones van aqui, en el formulario
      'enterado':forms.RadioSelect(choices=OPCIONES,attrs={'class':'labelinput'})
    }
