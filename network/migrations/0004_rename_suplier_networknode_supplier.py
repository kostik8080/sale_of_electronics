# Generated by Django 4.2.1 on 2024-07-11 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_remove_product_realizers_networknode_products_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='networknode',
            old_name='suplier',
            new_name='supplier',
        ),
    ]
