from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    foto = models.ImageField(upload_to='autores/')
    def __str__(self):
        return f"{self.nombre} ({self.nacionalidad})"

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=100)
    año = models.PositiveIntegerField()
    portada = models.ImageField(upload_to='libros/')
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')
    
