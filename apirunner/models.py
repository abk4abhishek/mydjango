from django.db import models
from django.utils import timezone
# Create your models here.



class Apirunner(models.Model):
    api_url = models.TextField()
    api_method = models.CharField(max_length=10)
    api_description = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)


    def __str__(self):
        return self.api_url
