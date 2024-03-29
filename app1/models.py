from django.db import models

class Classes(models.Model):
    title=models.CharField(max_length=32)
    m=models.ManyToManyField('Teacher')

class Teacher(models.Model):
    name=models.CharField(max_length=32)

class Student(models.Model):
    stuname=models.CharField(max_length=32)
    age=models.IntegerField()
    gender=models.BooleanField()
    cs=models.ForeignKey(Classes,on_delete=models.CASCADE)
