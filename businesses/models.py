from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


User = get_user_model()


class TimeStamps(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Store(TimeStamps, models.Model):
    name = models.CharField(max_length=150)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=150)

    def __str__(self) -> str:
        return f"{self.name} store"


class Category(TimeStamps, models.Model):
    title = models.CharField(max_length=30)
    store = models.ManyToManyField(Store)


class Inventory(models.Model):
    type = models.CharField(max_length=100)
    value = models.PositiveBigIntegerField()


class Product(TimeStamps, models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    description = models.TextField()
    sale_price = models.DecimalField(max_digits=15, decimal_places=2)
    cost_price = models.DecimalField(max_digits=15, decimal_places=2)
    inventory = models.OneToOneField(Inventory, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}"


class Sale(TimeStamps, models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    description = models.TextField()
    total_price = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.store.name} - sale"
