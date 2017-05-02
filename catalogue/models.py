from django.contrib.postgres.fields import IntegerRangeField
from django.contrib.postgres.validators import RangeMinValueValidator, RangeMaxValueValidator
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from datetime import datetime


class Bancnote(models.Model):
    validators_errors = {'par_length': 'Змініть номінал на коректний'}

    HRYVNA = 'Гривня'
    KARBOVANETS = 'Карбованець'

    TYPE_CHOICES = (
        (HRYVNA, 'Гривня'),
        (KARBOVANETS, 'Карбованець')
    )

    type = models.CharField(max_length=11, choices=TYPE_CHOICES, default=HRYVNA)
    par = models.PositiveIntegerField(validators=[MinValueValidator(1, validators_errors['par_length']),
                                                  MaxValueValidator(1000000, validators_errors['par_length'])])
    year = IntegerRangeField(validators=[RangeMinValueValidator(1917), RangeMaxValueValidator(datetime.now().year)])
    size = models.CharField(max_length=7)
    sign = models.CharField(max_length=20)
    desc = models.TextField(max_length=200)
    image = models.ImageField(upload_to='bons_images')

    def __str__(self):
        return str(self.par) + ' ' + self.type + ' ' + str(self.year.lower) + '-' + str(self.year.upper)
