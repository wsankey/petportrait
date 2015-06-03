# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubapi', '0002_auto_20150525_1308'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='updated_ad',
            new_name='updated_at',
        ),
    ]
