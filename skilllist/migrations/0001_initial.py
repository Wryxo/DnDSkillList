# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('prereq', models.CharField(max_length=200)),
                ('activation', models.CharField(max_length=200)),
                ('recharge', models.CharField(max_length=200)),
                ('castrange', models.CharField(max_length=200)),
                ('cost', models.CharField(max_length=200)),
                ('duration', models.CharField(max_length=200)),
            ],
        ),
    ]
