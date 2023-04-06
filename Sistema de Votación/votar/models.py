from django.db import models

class Region(models.Model):
  nombre = models.CharField(max_length=100,verbose_name='Región')
  def __str__(self):
    return self.nombre

class Comuna(models.Model):
  nombre = models.CharField(max_length=100,verbose_name='Comuna')
  def __str__(self):
    return self.nombre

class Candidato(models.Model):
  nombre = models.CharField(max_length=100,verbose_name='Comuna')
  def __str__(self):
    return self.nombre

class Enterado(models.Model):
  nombre = models.CharField(max_length=100,verbose_name='Comuna')
  def __str__(self):
    return self.nombre

class Votacion(models.Model):
  nombreApellido = models.CharField(max_length=100,verbose_name='Nombre y Apellido',null=False, blank=False)
  alias = models.CharField(max_length=100,verbose_name='Alias (opcional)',null=True, blank=True)
  cc = models.IntegerField(verbose_name='N° Cedula',unique=True,null=False, blank=False)
  email = models.EmailField(verbose_name='Email',null=False, blank=False)
  region = models.ForeignKey(Region,on_delete=models.CASCADE, null=False, blank=False,verbose_name='Region')
  comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE, null=False, blank=False)
  candidato = models.ForeignKey(Candidato,on_delete=models.CASCADE, null=False, blank=False)
  enterado=models.ForeignKey(Enterado,on_delete=models.CASCADE, null=False, blank=False)
  fecha=models.DateTimeField(auto_now_add=True)
