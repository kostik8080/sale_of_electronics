# Generated by Django 4.2.1 on 2024-07-10 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networknode',
            name='suplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='network.networknode', verbose_name='Поставщик'),
        ),
    ]
