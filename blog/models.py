from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(blank=True,null=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.title
