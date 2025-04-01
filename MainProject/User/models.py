from django.db import models
from Guest.models import *

# Create your models here.
    
class Feedback(models.Model):
    feedback_content=models.CharField(max_length=100)
    technician=models.ForeignKey('Admin.Technician',on_delete=models.SET_NULL,null=True)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

class Complaint(models.Model):
    complaint_title=models.CharField(max_length=50)
    complaint_content=models.CharField(max_length=50)
    complaint_date=models.DateField(auto_now_add=True)
    complaint_status=models.IntegerField(default=0)
    complaint_reply=models.CharField(max_length=100)
    technician=models.ForeignKey('Admin.Technician',on_delete=models.SET_NULL,null=True)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)    

class Servicebook(models.Model):
    Servicebook_details=models.CharField(max_length=100)
    Servicebook_address=models.CharField(max_length=100)
    Servicebook_date=models.DateField(auto_now_add=True)
    Servicebook_status=models.IntegerField(default=0)
    payment_status=models.IntegerField(default=0)
    category=models.ForeignKey('Admin.Category',on_delete=models.SET_NULL,null=True)
    brand=models.ForeignKey('Admin.Brand',on_delete=models.SET_NULL,null=True)  
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)     

class Ewastebooking(models.Model):
    ewastebooking_details=models.CharField(max_length=50)
    ewastebooking_date=models.DateField(auto_now_add=True)
    ewastebooking_status=models.IntegerField(default=0)
    ewastebooking_collectionpoint=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)   

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
    ]

    user = models.ForeignKey('Guest.User',on_delete=models.CASCADE)
    product = models.ForeignKey('Admin.Product', on_delete=models.CASCADE)  # ✅ Ensure this is correct
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Order {self.id}"
