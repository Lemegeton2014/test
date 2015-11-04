# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_auto_20151021_0902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bbs',
            name='cate',
        ),
        migrations.AddField(
            model_name='bbs',
            name='yang',
            field=models.ForeignKey(default=2, to='app01.Category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bbs',
            name='author',
            field=models.ForeignKey(to='app01.BBS_user'),
        ),
    ]
