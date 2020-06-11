from django.db import models
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
# Create your models here.
