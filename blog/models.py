from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField() # for the big text
    date_posted = models.DateTimeField(default=timezone.now)# the timezone parametere is for that we can change the time whenever we want
    author = models.ForeignKey(User, on_delete=models.CASCADE)# User is the name of the foregin key table and cascade for when deleting 
                                                                # the author all his posts is going to deleted with it
    
    def __str__(self):
        return self.title
