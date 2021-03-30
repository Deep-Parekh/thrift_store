from django.db import models

class Product(models.Model):
    # primary key/id field is added automatically
    name = models.CharField(max_length=100, blank=False, default='')
    price = models.IntegerField(blank=False, default=0)
    category = models.CharField(max_length=100, blank=False, default='')
    gender_choices = (('M', 'Male'), ('F', 'Female'), ('U', 'Unisex'))
    gender = models.CharField(max_length=1, choices=gender_choices, default='U')
    description = models.CharField(max_length=500, blank=False, default='')
    posted_on = models.DateTimeField(auto_now_add=True, blank=True)
    # seller_id = models.IntegerField(blank=True, null=True)
    # pictures
    # ...
