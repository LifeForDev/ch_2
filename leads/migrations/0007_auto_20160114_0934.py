# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0006_auto_20160113_2056'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lenguage',
            new_name='Language',
        ),
    ]
