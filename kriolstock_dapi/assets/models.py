from django.db import models
from users.models import User

# Create your models here.
class Documento(models.Model):
    documentos_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    upload_date = models.DateTimeField(auto_now_add=True)
    visibility = models.CharField(max_length=10)  # público, privado, restrito
    status = models.CharField(max_length=10)  # ativo, inativo
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    