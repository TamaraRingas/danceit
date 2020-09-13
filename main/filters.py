import django_filters
from .models import *

class VideoFilter(django_filters.FilterSet):
  class Meta:
    model = Video
    fields = '__all__'