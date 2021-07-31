from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class CustomUser(AbstractUser):
    user_type_data = ((1,"Admin"),(2,"Teacher",(3,"Student")))
    user_type=models.CharField(default=1,max_length=200)


class Admin(models.Model):
    admin =models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at = models.CharField(max_length=200)
    upated_at=models.CharField(max_length=200)


class Book(models.Model):

    name= models.CharField(max_length= 100,null=True)
    category=models.ForeignKey('Category',null=True,on_delete=models.SET_NULL)
    author=models.ForeignKey('Author',null=True,on_delete=models.SET_NULL)
    publish=models.ForeignKey('Publication',null=True,on_delete=models.SET_NULL)
    lng=models.CharField(max_length= 100,null=True)
    isbn=models.CharField( null=True,max_length=100)
    edition=models.CharField(max_length= 100,null=True,blank=True)
    edition_year=models.IntegerField( null=True,blank=True)
    copies= models.IntegerField(blank=True, null=True) 

    def __str__(self):
        return self.name                       
     
    class Meta:
         db_table = 'library_book'
            
class Category(models.Model):
    name=models.CharField(max_length= 100,null=True)
    desc =models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name
    class Meta:
       db_table = 'library_category' 

class Publication(models.Model):

    name=models.CharField(max_length= 100,null=True)
    address=models.CharField(max_length= 100,null=True,blank=True)

    def __str__(self):
        return self.name
    class Meta:
         db_table = 'library_publication'

class Author(models.Model):
    name=models.CharField(max_length= 100,null=True)
    phone=models.CharField(max_length= 100,null=True,blank=True)
    email=models.CharField(max_length= 100,null=True,blank=True)
    
    def __str__(self):
        return self.name
    class Meta:
         db_table = 'library_author'

class Student(models.Model):
    admin =models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    phone=models.CharField(max_length= 100,null=True)
    gender=models.CharField(max_length=200,null=True)
    picture=models.ImageField(upload_to ='images')
    session=models.CharField(max_length=200,null=True)
    dept=models.CharField(max_length= 100,null=True)
    deptid=models.IntegerField(null=True)
    join_date=models.CharField(max_length= 50,null=True)

    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    admin =models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    phone=models.CharField(max_length= 100,null=True)
    gender=models.CharField(max_length=200,null=True)
    picture=models.ImageField(upload_to ='images')
    dept=models.CharField(max_length= 100,null=True)
    join_date=models.CharField(max_length= 50,null=True)

    def __str__(self):
        return self.name


class Issue(models.Model):
    book= models.ForeignKey('Book',null=True,on_delete=models.SET_NULL)
    student=models.ForeignKey('Student',null=True,on_delete=models.SET_NULL)
    teacher= models.ForeignKey('Teacher',null=True,blank=True,on_delete=models.SET_NULL)
    issuedate=models.CharField(max_length= 50,null=True)
    returndate=models.CharField(max_length= 50,null=True,blank=True)
    latefee=models.FloatField(null=True,blank=True)
    

@receiver(post_save,sender=CustomUser)
def create_user(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            Admin.objects.create(admin=instance)
        if instance.user_type==2:
            Teacher.objects.create(admin=instance)
        if instance.user_type==1:
            Student.objects.create(admin=instance)

            
@receiver(post_save,sender=CustomUser)
def save_user(sender,instance,created,**kwargs):
    if instance.user_type ==1:
        instance.admin.save()
    if instance.user_type ==2:
        instance.teacher.save()
    if instance.user_type ==1:
        instance.student.save()


