from django.db import models

# Create your models here.
class Image(models.Model):
    desc = models.TextField(max_length=50)
    photo = models.ImageField(upload_to="myimage")
    date = models.DateTimeField(auto_now_add=True)