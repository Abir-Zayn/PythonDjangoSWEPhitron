from django.db import models

# Create your models here.

class studentModel(models.Model):
    name = models.CharField(max_length=30)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField()
    father_name = models.CharField(max_length=30)

    
    def __str__(self) -> str:
        return f'Name: {self.name}'