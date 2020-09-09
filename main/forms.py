from django import forms
from django.core.exceptions import ValidationError
from main.models import Video, Tag, Type

class AddVideoForm(forms.ModelForm):
  class Meta:
    model = Video

   # video_name = forms.CharField()
    #url = forms.URLField()
