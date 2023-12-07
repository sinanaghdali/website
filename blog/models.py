from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name
 
class post(models.Model):
    image = models.ImageField(upload_to= 'bolg/',default='blog/default.jpg')
    title = models.CharField(max_length=255)
    content = models.TextField()
    # tag
    category=models.ManyToManyField(category)
    author = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(null=True) 

    def __str__(self):          
        return '{} -{}'.format( self.title,self.id)

    def get_absolute_url(self):
        return reverse ('blog:single',kwargs = {'pid':self.id})
    