# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='last_login',
            field=models.DateTimeField(null=True, verbose_name='last login', blank=True),
        ),
        migrations.AddField(
            model_name='owner',
            name='password',
            field=models.CharField(default=12345, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]
