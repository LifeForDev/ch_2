# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0005_auto_20160113_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='card_number',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^[XTW0-9]{8,15}$', message=b'Card Number must be contain digital or X T W and have length from 8 to 15 characters', code=b'Invalid_card_number')]),
        ),
    ]
