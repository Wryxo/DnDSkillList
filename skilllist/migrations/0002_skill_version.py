# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skilllist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='version',
            field=models.IntegerField(default=3.5),
            preserve_default=False,
        ),
    ]
