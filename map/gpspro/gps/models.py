from django.db import models

# Create your models here.


class Asset(models.Model):
    asset_id=models.CharField(max_length=1000)
    asset_desc=models.TextField()
    asset_type=models.CharField(max_length=1000,default="")



class Asset_Cord(models.Model):
    asset_cor1=models.FloatField()
    asset_cor2=models.FloatField()
    asset_date_time=models.DateTimeField()
    asset=models.ForeignKey(Asset,on_delete=models.CASCADE)

    
    