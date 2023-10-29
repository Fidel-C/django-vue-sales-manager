from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.



User=get_user_model()
    
    
class TimeStamps(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)    
    updated_at=models.DateTimeField(auto_now=True)   
    class Meta:
        abstract=True 
        
        

class Store(TimeStamps,models.Model):
    name=models.CharField(max_length=150)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    location=models.CharField(max_length=150)
    
    def __str__(self) -> str:
        return f"{self.name} store"
    
    
    
class Product(TimeStamps,models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    sale_price=models.DecimalField(max_digits=15,decimal_places=2)
    cost_price=models.DecimalField(max_digits=15,decimal_places=2)
    inventory=models.PositiveBigIntegerField()
    store=models.ForeignKey(Store,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.title}"
    



class Sale(TimeStamps,models.Model):
    store=models.ForeignKey(Store, on_delete=models.CASCADE)
    total_price=models.DecimalField(max_digits=15,decimal_places=2)
    total_qty=models.PositiveBigIntegerField()
    
    def __str__(self) -> str:
        return f"{self.store.name} - sale"




class SaleItem(models.Model):
    product=models.ForeignKey(Product,null=True,on_delete=models.DO_NOTHING)
    quantity=models.PositiveBigIntegerField()
    sale=models.ForeignKey(Sale,models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.product.name}"


    
    
    
    
    
    
    
    