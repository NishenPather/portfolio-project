from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
   # author = models.ForeignKey(User,on_delete=models.CASCADE)

    def summary(self):
        return self.body[:100]

    def __str__(self):
        return self.title    
