# users/models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nitrogen = models.FloatField(blank=True, null=True)
    phosphorus = models.FloatField(blank=True, null=True)
    potassium = models.FloatField(blank=True, null=True)
    ph = models.FloatField(blank=True, null=True)
    rainfall = models.FloatField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    humidity = models.FloatField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'

class RecommendationHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nitrogen = models.FloatField()
    phosphorus = models.FloatField()
    potassium = models.FloatField()
    ph = models.FloatField()
    rainfall = models.FloatField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    recommended_crop = models.CharField(max_length=100)
    date_recommended = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user.username} - {self.recommended_crop} ({self.date_recommended.strftime("%Y-%m-%d")})'