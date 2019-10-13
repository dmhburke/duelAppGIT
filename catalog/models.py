from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from catalog.choices import *
from django.db.models import Sum, Count
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class PlayerModel(models.Model):
    number = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=30)
    HC = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='playerimages', blank=True, null=True)
    jacket = models.CharField(max_length=10,choices=YES_NO,blank=True, null=True)
    highfinish = models.IntegerField(blank=True, null=True)
    tournum = models.IntegerField(blank=True, null=True)
    nickname = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    total = models.DecimalField(max_digits=6, decimal_places=2, default=0, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-total']
