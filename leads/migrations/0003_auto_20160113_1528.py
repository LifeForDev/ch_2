# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_auto_20160113_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='professional',
            field=models.BooleanField(default=b'No', max_length=3, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
        ),
    ]
