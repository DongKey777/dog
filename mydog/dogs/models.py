from django.db import models

# Create your models here.
class Dog(models.Model):

    owner = models.ForeignKey('owners.Owner', on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    age = models.IntegerField()

    class Meta:
        db_table = 'Dogs'