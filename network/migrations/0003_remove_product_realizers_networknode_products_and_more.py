# Generated by Django 4.2.1 on 2024-07-11 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_alter_networknode_suplier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='realizers',
        ),
        migrations.AddField(
            model_name='networknode',
            name='products',
            field=models.ManyToManyField(related_name='nodes', to='network.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='release_date',
            field=models.DateField(verbose_name='Дата вохода в продажу'),
        ),
    ]
