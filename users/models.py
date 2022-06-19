from django.db import models

# Create your models here.
class EmailRecipients(models.Model):
    '''
    EmailRecepients model acts as blueprint for all email recepients on registation
    '''

    name = models.CharField(max_length=30)
    email = models.EmailField()
    