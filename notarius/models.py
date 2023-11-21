from django.db import models

class Report(models.Model):
    contractNumber = models.IntegerField()
    conrtractDate = models.DateField()
    clientname = models.CharField()
    image = models.ImageField(null=True, upload_to='images')

    def __str__(self):
        return self.clientname

