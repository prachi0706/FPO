# Generated by Django 3.0.7 on 2020-08-28 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20200828_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fpo_registeration',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='fpo_registeration',
            name='fpo_area',
            field=models.CharField(max_length=500),
        ),
    ]