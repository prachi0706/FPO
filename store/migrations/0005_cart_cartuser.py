# Generated by Django 3.0.7 on 2020-07-31 14:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0004_auto_20200729_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cartuser',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
