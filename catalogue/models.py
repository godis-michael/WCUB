from django.contrib.postgres.fields import IntegerRangeField
from django.contrib.postgres.validators import RangeMinValueValidator, RangeMaxValueValidator
from django.core.validators import MinValueValidator, MaxValueValidator

from django.db import models
from datetime import datetime, timezone


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
    year = IntegerRangeField(validators=[RangeMinValueValidator(1917), RangeMaxValueValidator(datetime.now().year + 1)])
    size = models.CharField(max_length=7)
    sign = models.TextField(max_length=250, blank=True)
    desc = models.TextField(max_length=1500)
    image = models.ImageField(upload_to='bons_images')

    def __str__(self):
        return str(self.par) + ' ' + self.type + ' ' + str(self.year.lower) + '-' + str(self.year.upper)


class Subscriber(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Article(models.Model):
    author = models.CharField(max_length=25, default='Адміністрація сайту')
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title
