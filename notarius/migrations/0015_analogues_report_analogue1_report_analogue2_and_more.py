# Generated by Django 4.2.7 on 2024-02-06 07:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notarius', '0014_vehicletechnicalcondition_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analogues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('analogueModel', models.CharField(max_length=255, null=True, verbose_name='Марка/модель автомобиля')),
                ('analogueYear', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2050)], verbose_name='Год выпуска автомобиля')),
                ('analogueLocation', models.CharField(null=True, verbose_name='Местоположение')),
                ('analogueDeterioration', models.DecimalField(decimal_places=2, max_digits=4, null=True, verbose_name='Физический износ, %')),
                ('analogueCost', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(100000000)], verbose_name='Стоимость')),
                ('analogueSourceOfInformation', models.CharField(max_length=255, null=True, verbose_name='Источник информации')),
                ('image', models.ImageField(blank=True, null=True, upload_to='analogues/vehicle/images')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='analogues/vehicle/images')),
                ('analogueTechnicalCondition', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='analoguetechnicalcondition', to='notarius.vehicletechnicalcondition', verbose_name='Техническое состояние объекта аналога')),
            ],
        ),
        migrations.AddField(
            model_name='report',
            name='analogue1',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='analogue1', to='notarius.analogues', verbose_name='Объект аналог1'),
        ),
        migrations.AddField(
            model_name='report',
            name='analogue2',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='analogue2', to='notarius.analogues', verbose_name='Объект аналог2'),
        ),
        migrations.AddField(
            model_name='report',
            name='analogue3',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='analogue3', to='notarius.analogues', verbose_name='Объект аналог3'),
        ),
    ]
