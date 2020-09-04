import django_filters
from . models import *
from django_filters import *

class BenchFilter(django_filters.FilterSet):
    name = CharFilter(field_name="name", lookup_expr='icontains')
    description = CharFilter(field_name="description", lookup_expr='icontains')
    date = DateFilter(field_name="date_created")
    class Meta:
        model = Bench
        fields = '__all__'
        exclude = ['image', 'tag']
