from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from os import path



_MAX_SIZE = 800

class Report(models.Model):
    appraiser = models.ForeignKey(User, on_delete=models.CASCADE, default='2', verbose_name="Оценщик")
    contractNumber = models.IntegerField(verbose_name="Номер договора", unique=True)
    conrtractDate = models.DateField(verbose_name="Дата договора")
    reportNumber = models.IntegerField(verbose_name="Номер отчета", null=True)
    dateOfAssessment = models.DateField(verbose_name="Дата оценки", null=True)
    dateOfReport = models.DateField(verbose_name="Дата составления отчета", null=True)
    documentsOfReport = models.TextField(verbose_name="Перечень используемых документов", null=True)
    purposeOfAssessment = models.ForeignKey('PurposeOfAssessment', on_delete=models.CASCADE, default='', verbose_name="Цель оценки", related_name='purpose', null=True, blank=True)
    clientType = models.ForeignKey('ClientType', on_delete=models.CASCADE, default='', verbose_name="Тип Заказчика", related_name='clienttype', null=True)
    clientName = models.CharField(max_length=255, verbose_name="ФИО клиента", null=True, blank=True)
    clientPersonData = models.ForeignKey('ClientPersonData', on_delete=models.CASCADE, default='', verbose_name="Данные клиента", related_name='clientdata', null=True )
    objectOfAssessment = models.ForeignKey('ObjectOfAssessment', on_delete=models.CASCADE, default='', verbose_name="Объект оценки", related_name='objectofassessment', null=True)
    analogue1 = models.ForeignKey('Analogues', on_delete=models.CASCADE, default='', verbose_name="Объект аналог1", related_name='analogue1', null=True)
    analogue2 = models.ForeignKey('Analogues', on_delete=models.CASCADE, default='', verbose_name="Объект аналог2", related_name='analogue2', null=True)
    analogue3 = models.ForeignKey('Analogues', on_delete=models.CASCADE, default='', verbose_name="Объект аналог3", related_name='analogue3', null=True)
    objectTotalCost = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100000000)],
                                                   verbose_name="Итоговая стоимость", null=True)
    objectTotalCostWord = models.CharField(max_length=555, verbose_name="Итоговая стоимость словами", null=True, blank=True)

    image = models.ImageField(null=True, upload_to='images')


    class Meta:
        verbose_name = "Список отчетов"
        verbose_name_plural = "Список отчетов"
        ordering = ['-pk']


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
    clientAdress = models.TextField( verbose_name="Адрес клиента", null=True)
    clientPasportSer = models.CharField(max_length=4, verbose_name="Серия паспорта", null=True)
    clientPasportNum = models.CharField(max_length=6, verbose_name="Номер паспорта", null=True)
    clientPasportDate = models.DateField(verbose_name="Дата выдачи паспорта", null=True)
    clientPasportGov = models.CharField(max_length=255, verbose_name="Кем выдан паспорт", null=True)

    class Meta:
        verbose_name = "Данные Заказчика"
        verbose_name_plural = "Данные Заказчика"
    def __str__(self):
        return self.clientPasportNum


class ObjectOfAssessment(models.Model):
    objectOfAssessmentModel = models.CharField(max_length=255, verbose_name="Марка/модель автомобиля", null=True)
    objectOfAssessmentYear = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2050)], verbose_name="Год выпуска автомобиля", null=True)
    objectOfAssessmentVIN = models.CharField(max_length=255, verbose_name="VIN автомобиля", null=True)
    objectRegistrationNumber = models.CharField(max_length=10, verbose_name="Государственный рег. знак", null=True)
    vehicleCategory = models.CharField(max_length=2, verbose_name="Категория транспортного средства", null=True)
    vehicleColor = models.CharField(max_length=15, verbose_name="Цвет транспортного средства", null=True)
    engine_power = models.CharField(max_length=10, verbose_name="Мощность двигателя, л.с. (кВт)", null=True)
    vehicleTechnicalCondition = models.ForeignKey('VehicleTechnicalCondition', on_delete=models.CASCADE, default='', verbose_name="Техническое состояние объекта оценки", related_name='vehicletechnicalcondition', null=True)
    physicalDeterioration = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Физический износ, %", null=True)

    class Meta:
        verbose_name = "Объект оценки"
        verbose_name_plural = "Объекты оценки"
    def __str__(self):
        return self.objectOfAssessmentModel



class VehicleTechnicalCondition(models.Model):
    shortTechnicalCondition = models.CharField(verbose_name="Краткое описание технического состояния", null=True)
    fullTechnicalCondition = models.CharField(verbose_name="Полное описание технического состояния", null=True)

    def __str__(self):
        return self.shortTechnicalCondition


class Analogues(models.Model):
    analogueModel = models.CharField(max_length=255, verbose_name="Марка/модель автомобиля", null=True)
    analogueYear = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2050)], verbose_name="Год выпуска автомобиля", null=True)
    analogueLocation = models.CharField(verbose_name="Местоположение", null=True)
    analogueTechnicalCondition = models.ForeignKey('VehicleTechnicalCondition', on_delete=models.CASCADE, default='',
                                                  verbose_name="Техническое состояние объекта аналога",
                                                  related_name='analoguetechnicalcondition', null=True)
    analogueDeterioration = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Физический износ, %",
                                                null=True)
    analogueCost = models.IntegerField(validators=[MinValueValidator(1000), MaxValueValidator(100000000)], verbose_name="Стоимость", null=True)
    analogueSourceOfInformation = models.CharField(max_length=255, verbose_name="Источник информации", null=True)
    offerDate = models.DateField(verbose_name="Дата объявления", null=True)
    analogueImage1 = models.ForeignKey('Images', on_delete=models.CASCADE, default='', verbose_name="Скриншот 1 аналога",
                                  related_name='analogueimage1', null=True)
    analogueImage2 = models.ForeignKey('Images', on_delete=models.CASCADE, default='', verbose_name="Скриншот 2 аналога",
                                  related_name='analogueimage2', null=True)
    analogueAdjustments = models.ForeignKey('Adjustments', on_delete=models.CASCADE, default='',
                                       verbose_name="Корректировки аналога",
                                       related_name='analogueadjustments', null=True)

    # def save(self, *args, **kwargs):
    #     # Сначала - обычное сохранение
    #     super(Analogues, self).save(*args, **kwargs)
    #
    #     # Проверяем, указан ли логотип
    #     if self.image:
    #         filename = f'media/{self.image.name}'
    #         filepath = self.image.path
    #         width = self.image.width
    #         height = self.image.height
    #
    #         max_size = max(width, height)
    #
    #         # Может, и не надо ничего менять?
    #         if max_size > _MAX_SIZE:
    #             # Надо, Федя, надо
    #             image = Image.open(filename)
    #             # resize - безопасная функция, она создаёт новый объект, а не
    #             # вносит изменения в исходный, поэтому так
    #             image = image.resize(
    #                 (round(width / max_size * _MAX_SIZE),  # Сохраняем пропорции
    #                 round(height / max_size * _MAX_SIZE)),
    #                 )
    #             # И не забыть сохраниться
    #             image.save(filename)


    def __str__(self):
        return self.analogueModel

class Images(models.Model):
    imageName = models.CharField(max_length=255, verbose_name="Заголовок изображения", null=True, blank=True)
    imageFile = models.ImageField(null=True, upload_to='analogues/vehicle/images', blank=True)

    def __str__(self):
        return self.imageFile


class Adjustments(models.Model):
    analogueDiscount = models.IntegerField(validators=[MinValueValidator(-30), MaxValueValidator(0)], verbose_name="Скидка на торг", null=True)
    analogueAdjustedDiscount = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(100000000)], verbose_name="Скорректированная после торга цена", null=True, max_digits=11, decimal_places=2)
    analogueTechnicalConditionAdjustment = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(1)], max_digits=5, decimal_places=4, verbose_name="Корректировка на физический износ",
                                                null=True)
    analogueAdjustedTechnicalCondition = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(100000000)], verbose_name="Скорректированная после износа цена", null=True, max_digits=11, decimal_places=2)
    analogueAveragePrice = models.DecimalField(
        validators=[MinValueValidator(0), MaxValueValidator(100000000)],
        verbose_name="Средневзвешенная цена", null=True, max_digits=11, decimal_places=2)


    def __str__(self):
        return self.analogueDiscount