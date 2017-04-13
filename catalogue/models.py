from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Bancnote(models.Model):
    validators_errors = {'year_length': 'Змініть рік на коректний',
                         'par_length': 'Змініть номінал на коректний'}

    type = models.CharField(max_length=11, default='Гривень')
    par = models.PositiveIntegerField(validators=[MinValueValidator(1, validators_errors['par_length']),
                                                  MaxValueValidator(2017, validators_errors['par_length'])])
    year_from = models.PositiveIntegerField(validators=[MinValueValidator(1917, validators_errors['year_length']),
                                                        MaxValueValidator(2017, validators_errors['year_length'])])
    year_to = models.PositiveIntegerField(validators=[MinValueValidator(1917, validators_errors['year_length']),
                                                      MaxValueValidator(2017, validators_errors['year_length'])])
    size = models.CharField(max_length=7)
    sign = models.CharField(max_length=20)
    desc = models.TextField(max_length=200)
    image = models.ImageField(upload_to='bons_images')

    def __str__(self):
        return str(self.par) + ' ' + self.type + ' ' + str(self.year_from) + '-' + str(self.year_to)
