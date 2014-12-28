from django.db import models

# Create your models here.
class info(models.Model):
  fname = models.CharField(max_length=15, default='1')
  lname = models.CharField(max_length=15, default='1')
  ph_no = models.CharField(max_length=13, primary_key=True)
  email = models.CharField(max_length=50, default='1')
  passwd = models.CharField(max_length=30, default='1')
  address = models.CharField(max_length=100, default='1')
  verify = models.BooleanField(default=False)
  GenderIsMale = models.BooleanField(default=False)

  rand = models.CharField(max_length=21, default='1')

  TotalOrders = models.IntegerField(default=0)


class orders(models.Model):
  custph = models.ForeignKey(info)
  metersquantity = models.CharField(max_length=50, default='0')
  status = models.CharField(max_length=3)
  DatePlaced = models.DateField()
  deliveryaddress = models.CharField(max_length=50, default='0')