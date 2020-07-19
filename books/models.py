from django.db import models
from login.models import User, UserManager

# Create your models here.
class Book(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  uploader = models.ForeignKey(User, related_name="upload_books",on_delete=models.CASCADE)
  users_who_like = models.ManyToManyField(User, related_name='liked_books') 
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)