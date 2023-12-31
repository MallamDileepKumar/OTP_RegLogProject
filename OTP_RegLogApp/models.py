from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=20)
    conf_password = models.CharField(max_length=20)
    mobile = models.IntegerField()
    def __str__(self):
        return self.username