# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_crs', '0007_remove_reviews_r_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shops',
            name='user',
        ),
    ]
