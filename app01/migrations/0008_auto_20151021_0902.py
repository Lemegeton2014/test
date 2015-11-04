# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_remove_bbs_cate'),
    ]

    operations = [
        migrations.AddField(
            model_name='bbs',
            name='cate',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bbs',
            name='author',
            field=models.ForeignKey(to='app01.Category'),
        ),
    ]
