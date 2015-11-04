# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbs',
            name='summary',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
    ]
