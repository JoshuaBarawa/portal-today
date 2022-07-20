from django.db import models
from cloudinary.models import CloudinaryField


class Item(models.Model):
    image = CloudinaryField()
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.name)
