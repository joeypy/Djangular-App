from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título", unique=True)
    description = models.TextField(max_length=256, blank=True, verbose_name="Descripción")
    price = models.DecimalField(default=0, max_digits=7, decimal_places=2, verbose_name="Precio")
    cover = models.ImageField(upload_to='assets/covers/', blank=True, verbose_name="Portada")
    published = models.DateField(blank=True, null=True, verbose_name="Publicado")
    is_published = models.BooleanField(default=False, verbose_name="En venta")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    class Meta():
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['id']

    def __str__(self):
        return self.title