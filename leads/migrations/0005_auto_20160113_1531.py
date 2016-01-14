# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import leads.validators


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0004_auto_20160113_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='expiry_date',
            field=models.DateField(blank=True, null=True, validators=[leads.validators.expireValid]),
        ),
    ]
