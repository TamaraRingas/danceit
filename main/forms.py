from django import forms
from django.core.exceptions import ValidationError
from main.models import Video, Tag, Type

class AddVideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('name', 'url', 'tags', )
        labels = {
            'name': 'Video Name',
            'url': 'Video URL',
            'tags': 'Tags',
        }


class AddTagFrom(forms.ModelForm):
  class Meta:
    model = Tag
    fields = ('name', 'videos', 'types', )
    labels = {
        'name': 'Tag Name',
        'videos': 'Videos',
        'tags': 'Tags',
    }

