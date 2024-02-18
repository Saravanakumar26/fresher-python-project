from django.db import models

class Register(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.CharField(max_length=50)
    mobile=models.IntegerField()
    qualification=models.CharField(max_length=20)
    cgpa=models.DecimalField(max_digits=3,decimal_places=2)
    objective=models.TextField()

def __str__(self):
    return self.name    


# Create your models here.
