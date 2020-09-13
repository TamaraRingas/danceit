import django_filters
from django_filters import CharFilter
from .models import *

class VideoFilter(django_filters.FilterSet):
  search = CharFilter(field_name="name", lookup_expr='icontains')
  class Meta:
    model = Video
    fields = '__all__'