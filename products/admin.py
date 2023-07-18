from django.contrib import admin
from products.models import Product, Tag, Comment
# Register your models here.
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Comment)

