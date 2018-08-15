from django.db import models

# Create your models here.
class customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    country_name = models.CharField(max_length=30)


    def __str__(self):
        return(self.first_name)
