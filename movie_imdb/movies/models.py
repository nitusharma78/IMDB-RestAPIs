from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class StreamPlatForm(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=100)
    website = models.CharField(max_length=200)


    def __str__(self):
        return self.name
    

class WatchList(models.Model):
    title = models.CharField(max_length=100)
    storyline = models.CharField(max_length=255)
    platform = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    

class Review(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveBigIntegerField() 
    description = models.CharField(max_length=200, null=True)
    watchList = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name='reviews')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.rating)+" "+str(self.watchList.title)
