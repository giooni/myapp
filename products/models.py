from django.db import models
from users.models import User

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
class Product(models.Model):
    tags = models.ManyToManyField(Tag, blank=True)
    title = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    model = models.CharField(max_length=120)
    image = models.ImageField(upload_to='products', blank=True)
    category = models.CharField(max_length=120)
    createtime = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.title} - {self.model}'
    
    
class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    txt = models.TextField()
    createtime = models.DateTimeField(auto_now_add=True)
    def __str__(self) ->str:
        return self.user.username