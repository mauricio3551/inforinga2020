# Generated by Django 3.0 on 2020-09-26 04:24

import apps.post.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20200926_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='portada',
            field=models.ImageField(blank=True, null=True, upload_to='post/', validators=[apps.post.models.validar_extension]),
        ),
    ]
