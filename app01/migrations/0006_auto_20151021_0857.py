# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_auto_20151021_0843'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bbs',
            old_name='category',
            new_name='cate',
        ),
    ]
