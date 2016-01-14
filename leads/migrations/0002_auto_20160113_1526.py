# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='gender',
            field=models.CharField(default=b'Male', max_length=12, choices=[(b'Male', b'Male'), (b'Female', b'Female')]),
        ),
        migrations.AlterField(
            model_name='lead',
            name='professional',
            field=models.BooleanField(default=b'Yes', max_length=3, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
        ),
    ]
