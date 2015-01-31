from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class tweet(models.Model):
    text = models.CharField(max_length = 140)
    searchterm = models.CharField(max_length = 40)
    user = models.CharField(max_length = 15)
    sentiment = models.CharField(max_length = 3) # True for pos, False for neg
    datetime = models.DateTimeField(auto_now_add=True)
    lat = models.FloatField(validators = [MinValueValidator(-90.0), MaxValueValidator(90.0)], null=True)
    lng = models.FloatField(validators = [MinValueValidator(-180.0), MaxValueValidator(180.0)], null=True)
    class Meta:
        app_label = 'heatmap'