from django.db import models

# Create your models here.
from django.db.models import DateTimeField


class EmpNew(models.Model):
    emp_name = models.CharField(max_length=64,null=True)
    emp_id = models.AutoField(primary_key=True)
    gender = models.IntegerField(null=True,choices=((1,'男'),(2,'女') ))
    mobile_phone = models.CharField(max_length=64,null=True)

    class Meta:
        db_table ='empnew'

    def __str__(self):
        return self.emp_name



class Student(models.Model):
    SEX = ((1, '男'), (2, '女'))
    name = models.CharField(max_length=10,null=True,)
    id = models.AutoField(primary_key=True)
    sex = models.IntegerField(null=True,choices=SEX)
    addr = models.CharField(max_length=64,null=True)
    createDate = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'student'
        ordering = ['-createDate',]

    def __str__(self):
        return  self.name+ str(self.id)



class Emp(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64,null=True,verbose_name='姓名')
    age = models.IntegerField(null=True,verbose_name='年龄')
    sex = models.CharField(max_length=1,null=True,verbose_name='性别')
    birthDay = models.DateField(verbose_name='生日')

    class Meta:
        db_table = 'emp'
        ordering = ['-age']
