from django.db import models

# Create your models here.
class VerifyResult():
    str1 = models.CharField(max_length=100)
    str2 = models.CharField(max_length=100)
    result = models.CharField(max_length=10)