from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField( max_length=250)
    author=models.CharField( max_length=250)
    slug=models.CharField( max_length=250)
    views=models.IntegerField(default=0)
    content=models.TextField()
    timestamp=models.DateTimeField(blank=True)

    def __str__(self):
        return self.title +" By " + self.author


class BlogComment(models.Model):
    id=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)    
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp=models.DateTimeField(default=now)    

    def __str__(self) :
        return f"{self.comment} ...  by {self.user.first_name}"