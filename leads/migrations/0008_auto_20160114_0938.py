# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0007_auto_20160114_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='lead',
            field=models.ForeignKey(related_name='languages', to='leads.Lead'),
        ),
    ]
