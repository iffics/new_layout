# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_crs', '0006_auto_20170313_0953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='r_user',
        ),
    ]
