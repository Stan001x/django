from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Report(models.Model):
    appraiser = models.ForeignKey(User, on_delete=models.CASCADE, default='2', verbose_name="Оценщик")
    contractNumber = models.IntegerField(verbose_name="Номер договора", unique=True)
    conrtractDate = models.DateField(verbose_name="Дата договора")
    purposeOfAssessment = models.ForeignKey('PurposeOfAssessment', on_delete=models.CASCADE, default='', verbose_name="Цель оценки", related_name='purpose', null=True, blank=True)
    clientType = models.ForeignKey('ClientType', on_delete=models.CASCADE, default='', verbose_name="Тип Заказчика", related_name='clienttype', null=True)
    clientName = models.CharField(max_length=255, verbose_name="ФИО клиента", null=True)
    clientAdress = models.TextField( verbose_name="Адрес клиента", null=True)
    clientPasportSer = models.CharField(max_length=4, verbose_name="Серия паспорта", null=True)
    clientPasportNum = models.CharField(max_length=6, verbose_name="Номер паспорта", null=True)
    clientPasportDate = models.DateField(verbose_name="Дата выдачи паспорта", null=True)
    clientPasportGov = models.CharField(max_length=255, verbose_name="Кем выдан паспорт", null=True)
    objectOfAssessmentModel = models.CharField(max_length=255, verbose_name="Марка/модель автомобиля", null=True)
    objectOfAssessmentYear = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2050)], verbose_name="Год выпуска автомобиля", null=True)
    objectOfAssessmentVIN = models.CharField(max_length=255, verbose_name="VIN автомобиля", null=True)



    image = models.ImageField(null=True, upload_to='images')


    class Meta:
        verbose_name = "Список отчетов"
        verbose_name_plural = "Список отчетов"


    def __str__(self):
        return self.clientName

    def get_absolute_url(self):
        return reverse('notarius:report', kwargs={'pk': self.pk})



class PurposeOfAssessment(models.Model):
    purposeOfAssessment1 = models.CharField(verbose_name="Цель оценки", default=1)

    class Meta:
        verbose_name = "Цель оценки"
        verbose_name_plural = "Цель оценки"
    def __str__(self):
        return self.purposeOfAssessment1


class ClientType(models.Model):
    clientType = models.CharField(null=True)

    class Meta:
        verbose_name = "Тип Заказчика"
        verbose_name_plural = "Тип Заказчика"
    def __str__(self):
        return self.clientType

class ClientPersonData(models.Model):
    clientName1 = models.CharField(max_length=255, verbose_name="ФИО клиента1", null=True)
    clientAdress1 = models.TextField( verbose_name="Адрес клиента1", null=True)
    clientPasportSer1 = models.CharField(max_length=4, verbose_name="Серия паспорта1", null=True)
    clientPasportNum1 = models.CharField(max_length=6, verbose_name="Номер паспорта1", null=True)
    clientPasportDate1 = models.DateField(verbose_name="Дата выдачи паспорта1", null=True)
    clientPasportGov1 = models.CharField(max_length=255, verbose_name="Кем выдан паспорт1", null=True)


