from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 120)
    content = models.TextField()
    active = models.BooleanField(default = True)
    
    def get_absolute_url(self):
        # appname (Blog) tells Django where to source for the url.py file
        return reverse("Blog:article-det", kwargs={"id" : self.id})
    