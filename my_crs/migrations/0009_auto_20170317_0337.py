# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_crs', '0008_remove_shops_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='r_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
        ),
        migrations.AddField(
            model_name='shops',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
        ),
    ]
