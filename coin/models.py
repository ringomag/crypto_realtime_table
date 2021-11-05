from django.db import models

class Coin(models.Model):
    name =  models.CharField(max_length=100)
    price = models.FloatField(default=0, blank=True)
    rank = models.IntegerField(default=0, blank=True)
    symbol = models.CharField(max_length=50)
    image = models.URLField(blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['rank']