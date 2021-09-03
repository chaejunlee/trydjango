from django.db import models

# Create your models here.
class Product(models.Model):
  title       = models.CharField(max_length=120) # max_lenght = required
  description = models.TextField(blank=True, null=True)
  price       = models.DecimalField(decimal_places=2, max_digits=10000)
  summary     = models.TextField(blank=True, null=False)
  # blank=False -> have to fill the area out (Field is rendered Bold)
  # blank=True -> don't have to fill the area out
  # null=True -> it can be empty in the DB
  # null=False -> it can not be empty in the DB
  featured    = models.BooleanField()