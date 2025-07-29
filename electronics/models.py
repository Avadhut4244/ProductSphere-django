from django.db import models
from django.contrib.auth.models import User  # Import the User model

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the creator
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to="post_images/", null=True)

    def __str__(self):
        return self.name
