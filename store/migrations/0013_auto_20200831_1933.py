# Generated by Django 3.0.7 on 2020-08-31 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20200831_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fpo_registeration',
            name='fpo_username',
            field=models.CharField(max_length=50),
        ),
    ]
