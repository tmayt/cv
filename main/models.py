from django.db import models

class Profile(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=13)
    linkedin = models.URLField(max_length=200)
    city = models.CharField(max_length=50)
    image = models.ImageField(upload_to='profile')

    def __str__(self):
        return self.full_name


class Education(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateField()
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.title
    
class Qualification(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text
