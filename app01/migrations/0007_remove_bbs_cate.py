# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_auto_20151021_0857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bbs',
            name='cate',
        ),
    ]
