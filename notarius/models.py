from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Report(models.Model):
    appraiser = models.ForeignKey(User, on_delete=models.CASCADE, default='2')
    contractNumber = models.IntegerField()
    conrtractDate = models.DateField()
    clientname = models.CharField()
    image = models.ImageField(null=True, upload_to='images')

    def __str__(self):
        return self.clientname

    def get_absolute_url(self):
        return reverse('notarius:report', kwargs={'pk': self.pk})

