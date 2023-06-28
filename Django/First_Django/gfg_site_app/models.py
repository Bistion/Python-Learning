from django.db import models
from datetime import datetime

class GeeksModel(models.Model):
    # Field Names
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_on = models.DateTimeField(default=datetime.now)
    image = models.ImageField(upload_to="images/%Y/%m/%d")

    # Rename the instances of the model with their title name
    def __str__(self) -> str:
        return self.title

# Create your models here.
