from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

#TODO: Category: samsung(smartphones)
#TODO: Laptops --> Acer, MacBook, asus
#TODO: Accesories --> earphones, powerbank
#TODO: 2 products for each category


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(primary_key=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='children')

    def __str__(self):
        if self.parent:
            return f'{self.parent} --> {self.title}'
        return self.title

class Product(models.Model):
    STATUS_CHOICES = (
        ('in stock', 'IN STOCK'),
        ('out of stock', 'OUT OF STOCK'),
        ('awaiting', 'AWAITING')
    )
    name = models.CharField(max_length=155)
    status = models.CharField(choices=STATUS_CHOICES, max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='prod_images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')


    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('detail', kwargs={'product_id': self.pk})

    def __str__(self) -> str:
        return self.name

