from django.db import models

# Se crean las clases necesarias.

class Docente(models.Model):
    cedula = models.CharField(max_length=30, unique=True)
    nombres = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    titulo = models.CharField(max_length=30)
    def __str__(self):
        return "%s %s %s %s" % (self.cedula, 
                self.nombres,
                self.apellido,
                self.titulo)

class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    numcred = models.CharField(max_length=100)
    progacad = models.CharField(max_length=100)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s %s" % (self.nombre,self.numcred, self.progacad)

