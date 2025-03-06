from django.db import models

# Create your models here.

class CollectedEwaste(models.Model):
    collectedewastedumped_date=models.DateField(auto_now_add=True)
    collectedewaste_weight=models.CharField(max_length=100)
    Ewaste=models.ForeignKey('Admin.Assignewastebooking',on_delete=models.SET_NULL,null=True)
    yard=models.ForeignKey('Admin.Yard',on_delete=models.SET_NULL,null=True)