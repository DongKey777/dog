from django.db import models

# Create your models here.
from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    age = models.IntegerField()

    class Meta:
        db_table = 'owners'

