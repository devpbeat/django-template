from django.db import models
from base.models import TimeStampModel

# Create your models here.
class Receta(TimeStampModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='recipe_images/')
    
    def __str__(self):
        return f"{self.title} - {self.created_at}"
    