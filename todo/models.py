from django.db import models

# Create your models here.
#link with db
class TodoItems(models.Model):
    content=models.TextField()
