from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField("Nome", max_length=255)
    image = models.ImageField("Foto do Produto", upload_to="products/", blank=True, null=True)
    stock = models.IntegerField("Estoque")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name