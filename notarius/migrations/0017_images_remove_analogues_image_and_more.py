# Generated by Django 4.2.7 on 2024-02-07 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notarius', '0016_analogues_offerdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageName', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок изображения')),
                ('imageFile', models.ImageField(blank=True, null=True, upload_to='analogues/vehicle/images')),
            ],
        ),
        migrations.RemoveField(
            model_name='analogues',
            name='image',
        ),
        migrations.RemoveField(
            model_name='analogues',
            name='image1',
        ),
        migrations.AddField(
            model_name='analogues',
            name='analogueImage1',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='analogueimage1', to='notarius.images', verbose_name='Скриншот 1 аналога'),
        ),
        migrations.AddField(
            model_name='analogues',
            name='analogueImage2',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='analogueimage2', to='notarius.images', verbose_name='Скриншот 2 аналога'),
        ),
    ]
