from django.db import models
from tinymce.models import HTMLField

class Comment(models.Model):
    name= models.CharField(max_length=100)
    text= models.TextField()
    date= models.DateTimeField(auto_now_add=True)
    comments= models.ForeignKey("blog.comment", on_delete=models.CASCADE)
        
    def __str__(self):
        return self.name
    

class Blog(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to="blog")
    date_update = models.DateField(auto_now=True)
    date_create = models.DateField(auto_now_add=True)
    tags = models.TextField(help_text="split keyword by comma")
    content = HTMLField()
    
    def __str__(self):
        return self.title
    