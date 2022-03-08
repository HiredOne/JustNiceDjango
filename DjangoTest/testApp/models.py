from django.db import models
from django.urls import reverse

# Create your models here.
class TestApp(models.Model): # Essentially OOP
    title = models.CharField(max_length = 120) #max_length = required
    description = models.TextField(blank = True, null = True)
    price = models.FloatField()
    summary = models.TextField(default = "this is cool!")

    def get_absolute_url(self):
		# This version uses django's reverse function. Upside about this function is
        # that if a part of the path is modified in urls.py, this function will 
        # ensure that the function still works. 
        # First arg is the name of the path, second arg is kwargs which takes in a 
        # dic, the key must match the kwarg that is used in the path and the value
        # will be the value of the model that is to be added as an extension
        return reverse("testApp:product-det", kwargs = {"my_id" : self.id}) #f"/product/{self.id}/"