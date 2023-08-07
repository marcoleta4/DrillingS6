from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
# Create your models here.
@receiver(post_save, sender=User)
def assign_permissions(sender, instance, created, **kwargs):
    if created:
        # Asignar permisos
        content_type = ContentType.objects.get_for_model(Auto)
        #permission_add_auto = Permission.objects.get(content_type=content_type, codename='add_auto')
        permission_view_catalog = Permission.objects.get(content_type=content_type, codename='visualizar_catalogo')
        instance.user_permissions.add(permission_view_catalog)
        #instance.user_permissions.add(permission_add_auto, permission_view_catalog)

        # Establecer como staff
        #instance.is_staff = True
        #instance.save()

class BoardsModel(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    modificado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Auto(models.Model):
    CATEGORIA_CHOICES = (
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga'),
    )

    MARCA_CHOICES = (
        ('Fiat', 'Fiat'),
        ('Chevrolet', 'Chevrolet'),
        ('Ford', 'Ford'),
        ('Toyota', 'Toyota'),
    )

    marca = models.CharField(max_length=20, choices=MARCA_CHOICES)
    modelo = models.CharField(max_length=100)
    serialCarroceria = models.CharField(max_length=50)
    serialMotor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    precio = models.IntegerField()
    fechaCreacion = models.DateField()
    fechaModificacion = models.DateField(auto_now=True)

    def __str__(self):
        texto = "{0} {1} ({2}) - Serial Motor: {3} - Categoría: {4} - Precio: {5} - Fecha Creación: {6} - Fecha Modificación: {7}"
        return texto.format(self.marca, self.modelo, self.serialCarroceria, self.serialMotor, self.categoria, self.precio, self.fechaCreacion, self.fechaModificacion)

    class Meta:
        permissions = [("visualizar_catalogo", "Visualizar Catalogo")]