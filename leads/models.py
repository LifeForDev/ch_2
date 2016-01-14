from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

from .validators import expireValid


class Lead(models.Model):

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    PROFESSIONAL_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )

    name = models.CharField(max_length=32)
    gender = models.CharField(max_length=12, choices=GENDER_CHOICES, default='Male')
    card_number = models.CharField(
        max_length=15,
        blank=True,
        validators=[
            RegexValidator(
                regex=r'^[XTW0-9]{8,15}$',
                message='Card Number must be contain digital or X T W' +
                        ' and have length from 8 to 15 characters',
                code='Invalid_card_number'
            )
        ]
    )
    expiry_date = models.DateField(blank=True, null=True, validators=[expireValid])
    professional = models.CharField(max_length=3, default='No', choices=PROFESSIONAL_CHOICES)

    def __unicode__(self):
        return self.name

    def clean(self):
        if bool(self.card_number) != bool(self.expiry_date):
            raise ValidationError('Check please Card number or Expiry Date')


class Language(models.Model):
    name = models.CharField(max_length=128)
    lead = models.ForeignKey('Lead', related_name='languages')

    def __unicode__(self):
        return self.name
