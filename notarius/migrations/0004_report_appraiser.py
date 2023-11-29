# Generated by Django 4.2.7 on 2023-11-29 09:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notarius', '0003_alter_report_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='appraiser',
            field=models.ForeignKey(default='2', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
