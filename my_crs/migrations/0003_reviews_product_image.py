# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_crs', '0002_shops_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='product_image',
            field=models.FileField(null=True, blank=True, upload_to=''),
        ),
    ]
