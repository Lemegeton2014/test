# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0009_auto_20151021_0908'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bbs',
            old_name='yang',
            new_name='category',
        ),
    ]
