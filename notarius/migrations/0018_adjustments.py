# Generated by Django 4.2.7 on 2024-02-08 06:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notarius', '0017_images_remove_analogues_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adjustments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('analogueDiscount', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(-30), django.core.validators.MaxValueValidator(0)], verbose_name='Скидка на торг')),
                ('analogueAdjustedDiscount', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000000)], verbose_name='Скорректированная после торга цена')),
                ('analogueTechnicalConditionAdjustment', models.DecimalField(decimal_places=4, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)], verbose_name='Корректировка на физический износ')),
                ('analogueAdjustedTechnicalCondition', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000000)], verbose_name='Скорректированная после износа цена')),
                ('analogueAveragePrice', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000000)], verbose_name='Средневзвешенная цена')),
            ],
        ),
    ]
