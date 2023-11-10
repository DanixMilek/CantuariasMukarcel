from django.db import models

class Pintura(models.Model):
    id= models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    precio=models.DecimalField(max_digits=9,decimal_places=2,default=0)
    descripcion=models.CharField(max_length=300)
    imagen=models.ImageField(upload_to='media/')

    def __str__(self):
        return str(self.nombre) + ": $" + str(self.precio)    
class Curso(models.Model):
    id= models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    precio=models.DecimalField(max_digits=9,decimal_places=2,default=0)
    descripcion=models.CharField(max_length=300)
    imagen=models.ImageField(upload_to='media/',blank=True,default='curso_default.jpeg')
    
    def __str__(self):
        return str(self.nombre) + ": $" + str(self.precio)    