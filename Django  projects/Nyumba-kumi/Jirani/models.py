
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    logo = CloudinaryField('image', blank=True)
    health_dept = models.IntegerField(null=True, blank=True)
    police_dept = models.IntegerField(null=True, blank=True)
    admin = models.IntegerField("neighbourhood admin", blank=False, default=1)
    description = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    def create_neighbourhd(self):
        self.save()

    @classmethod
    def delete_neighbourhd(cls, pk):
        cls.objects.filter(pk=pk).delete()

    @classmethod
    def find_neighbourhd(cls, id):
        search_results = cls.objects.filter(id=id)
        return search_results

    def update_neighbourhd(self, name):
      self.name = name
      self.save()

