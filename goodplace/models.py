from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MatZip(models.Model):
    MatZip_Name = models.CharField(max_length=20)
    MatZip_Address = models.CharField(max_length=50)
    MatZip_Time = models.CharField(max_length=100)
    MatZip_PhoneN = models.CharField(max_length=15)
    MatZip_DesC = models.CharField(max_length=50)
    MatZip_rating = models.IntegerField(default=0)
    MatZip_latitude = models.CharField(max_length=20)
    MatZip_longitude = models.CharField(max_length=20)
    MatZip_review_count = models.IntegerField(default=0)

    def __str__(self):
        return self.MatZip_Name

class Review(models.Model):
    r_content = models.CharField(max_length=200)
    r_author = models.ForeignKey(User, on_delete=models.CASCADE)
    r_restaurant = models.ForeignKey(MatZip, on_delete=models.CASCADE)
    r_time = models.DateTimeField(auto_now=True)
    r_rating = models.IntegerField(default=0)

    def __str__(self):
        return self.r_content