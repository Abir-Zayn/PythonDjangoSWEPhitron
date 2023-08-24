from django.db import models

# Create your models here.
class student(models.Model):

    # automatically add value sequentially can be also act as an primary key.
    # id = models.AutoField()
    
    name = models.CharField(max_length=100)
    #If the name length greater than 100 will throw an exception
    
    age = models.IntegerField()
    #if no value has added then by default 18 will be added.
    # age = models.IntegerField(default=18)

    email =models.EmailField(null =True, blank=True)
    # 2nd migration
    
    address = models.TextField(null=True ,blank=True)
    # 1st migration-> It will consider even the null values now
    # After adding the null and blank now we will migrate. Previously there weren't any changes. But now
    # there has been change so it will create another file to detect the changes.
    
    # Output after migaration ->    
    # ~home/migrations/0002_alter_student_address.py
    # ~ - Alter field address on student
    
    
    #!In 3rd migration we will remove these values
    #image = models.ImageField()
    #files = models.FileField()
    
    #*DateTimeField,Choices Field, Floar Field there are a lot of field available

class Car (models.Model):
    car_name = models.CharField(max_length=200)
    speed = models.IntegerField(default=50)
    

class superCar(models.Model):
    s_car_brand = models.CharField(max_length=100)
    s_car_speed = models.IntegerField(default=20)
    

# & Django Shell command 
'''
saving the data objects in the database via shell 
1. s1=student(name="Abir Zayn", age=21, email='abir@gmail.com', address="London, UK")
s1.save()

Another way >>
2. s2 = student.objects.create(name="tausif", age=23, email="tausif21@gmail.com", address="India")

To get the data from the objects that have created and exist in the database 
student.objects.all()[0].name
Output: 'Abir Zayn'
'''
