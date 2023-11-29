from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    appraiser = models.ForeignKey(User, on_delete=models.CASCADE, default='2')
    contractNumber = models.IntegerField()
    conrtractDate = models.DateField()
    clientname = models.CharField()
    image = models.ImageField(null=True, upload_to='images')

    def __str__(self):
        return self.clientname

