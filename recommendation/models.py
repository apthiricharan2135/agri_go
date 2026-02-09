from django.db import models

# Create your models here.
from django.db import models

class Crop(models.Model):
    #Name of the crop
    name = models.CharField(max_length=100)
    
    #Soil type
    SOIL_TYPES = [
        ('sandy', 'Sandy'),
        ('loamy', 'Loamy'),
        ('clay', 'Clay'),
        ('black', 'Black'),
    ]
    soil_type = models.CharField(max_length=50, choices=SOIL_TYPES)
    
    #Water availability
    WATER_LEVELS = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    water_requirement = models.CharField(max_length=20, choices=WATER_LEVELS)
    
    #Season
    SEASONS = [
        ('summer', 'Summer'),
        ('monsoon', 'Monsoon'),
        ('winter', 'Winter'),
    ]
    season = models.CharField(max_length=20, choices=SEASONS)
    
    #Max budget needed (e.g., 5000)
    budget_range = models.IntegerField()
    
    #Guidance info
    advantages = models.TextField()
    cultivation_process = models.TextField()
    yield_tips = models.TextField()

    def __str__(self):
        return self.name