# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skilllist', '0002_skill_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='path',
            field=models.CharField(max_length=200, default='Unlinked Skills'),
            preserve_default=False,
        ),
    ]
