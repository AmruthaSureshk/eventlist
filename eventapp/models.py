from django.db import models


# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    location = models.CharField(max_length=250)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    img = models.ImageField(upload_to='picture', blank=True)
    published = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.title
