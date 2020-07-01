from django.db import models

# Create your models here.
class Mail(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

class Attachments(models.Model):
    location =models.ForeignKey('Mail',on_delete=models.CASCADE)
    file = models.FileField(upload_to='media/',blank=True,default='',verbose_name='file')
