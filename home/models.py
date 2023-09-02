from django.db import models

# Create your models here.

class Contact(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField( max_length=250)
    email=models.EmailField( max_length=100)
    phone=models.IntegerField()
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return 'Message From '+self.name

    