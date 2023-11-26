from django.db import models

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
