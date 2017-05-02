from django import forms
import django_filters

from .models import Bancnote


class BancnoteFilter(django_filters.FilterSet):
    type = django_filters.ChoiceFilter(name='type', choices=Bancnote.TYPE_CHOICES,
                                       widget=forms.RadioSelect(attrs={'class': 'radio'}), empty_label=None)
    par_gt = django_filters.NumberFilter(name='par', lookup_expr='gte', widget=forms.Select)
    par_lt = django_filters.NumberFilter(name='par', lookup_expr='lte', widget=forms.Select)
    year = django_filters.NumericRangeFilter(name='year', lookup_expr='adjacent_to')

    class Meta:
        model = Bancnote
        fields = ['type', 'par_gt', 'par_lt', 'year']
