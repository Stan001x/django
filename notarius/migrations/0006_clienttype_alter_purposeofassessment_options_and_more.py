# Generated by Django 4.2.7 on 2024-01-29 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notarius', '0005_purposeofassessment_alter_report_appraiser_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientType', models.CharField(null=True)),
            ],
            options={
                'verbose_name': 'Тип Заказчика',
                'verbose_name_plural': 'Тип Заказчика',
            },
        ),
        migrations.AlterModelOptions(
            name='purposeofassessment',
            options={'verbose_name': 'Цель оценки', 'verbose_name_plural': 'Цель оценки'},
        ),
        migrations.AlterModelOptions(
            name='report',
            options={'verbose_name': 'Список отчетов', 'verbose_name_plural': 'Список отчетов'},
        ),
        migrations.RemoveField(
            model_name='report',
            name='clientname',
        ),
        migrations.AddField(
            model_name='report',
            name='clientType',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clienttype', to='notarius.clienttype', verbose_name='Тип Заказчика'),
        ),
    ]