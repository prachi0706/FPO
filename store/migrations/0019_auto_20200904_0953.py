# Generated by Django 3.0.7 on 2020-09-04 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_auto_20200904_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_img1',
            field=models.ImageField(default='images/product/cart.png', upload_to='images/product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_img2',
            field=models.ImageField(default='images/product/cart.png', upload_to='images/product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_img3',
            field=models.ImageField(default='images/product/cart.png', upload_to='images/product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_img4',
            field=models.ImageField(default='images/product/cart.png', upload_to='images/product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_img5',
            field=models.ImageField(default='images/product/cart.png', upload_to='images/product'),
        ),
    ]
