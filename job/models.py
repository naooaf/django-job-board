from django.db import models
CHOICES = (
        ('1', 'Full Time'),
        ('2', 'Part Time')
)
# Create your models here.
class job(models.Model):
    title = models.CharField(max_length=100, default='')
    job_type= models.CharField(max_length=300, choices = CHOICES, default='')
    description = models.TextField(max_length=1000, default='')
    vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    exprience=models.IntegerField(default=1)
    date= models.DateTimeField(auto_now=True)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)
    
    
    
    
    def __str__(self) :
        return self.title
   
   

 
class Category(models.Model):
    name = models.CharField(max_length=15, default='')
    
    def __str__(self) :
        return self.name
     