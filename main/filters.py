import django_filters
from django_filters import CharFilter
from .models import *

class VideoFilter(django_filters.FilterSet):
  class Meta:
    model = Video
    fields = '__all__'