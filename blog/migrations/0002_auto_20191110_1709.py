# Generated by Django 2.2.7 on 2019-11-10 17:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='address_vendor',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='pincode',
            field=models.CharField(default='000000', max_length=6),
        ),
    ]