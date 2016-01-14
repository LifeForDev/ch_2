# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import leads.validators
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('gender', models.CharField(max_length=12, choices=[(b'Male', b'Male'), (b'Female', b'Female')])),
                ('card_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^[XTW0-9]{8-15}$', message=b'Card Number must be contain digital or X T W and have length from 8 to 15 characters', code=b'Invalid_card_number')])),
                ('expiry_date', models.DateField(blank=True, validators=[leads.validators.expireValid])),
                ('professional', models.BooleanField(max_length=3, choices=[(b'Yes', b'Yes'), (b'No', b'No')])),
            ],
        ),
        migrations.CreateModel(
            name='Lenguage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('lead', models.ForeignKey(to='leads.Lead')),
            ],
        ),
    ]
