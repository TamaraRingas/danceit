from django import forms
from django.forms import ModelForm 
from django.db import models
from django.core import validators 
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import requests
from main.models import Video, Tag, Type

class AddVideoForm(ModelForm):

    def clean_name(self):
      data = self.cleaned_data['name']

      if len(data) > 100: 
          raise ValidationError(_('Invalid Video Name'))
      
      return data

    def clean_url(self):
        url_data = self.cleaned_data['url']
        #
        return url_data
        
    def clean_tags(self):
        tag_data = self.cleaned_data['tags']
        #
        return tag_data

    class Meta:
        model = Video
        fields = ['name', 'url', 'tags', ]
        labels = {
            'name': 'Video Name',
            'url': 'Video URL',
            'tags': 'Tags',
        }

    
class AddTagFrom(forms.ModelForm):
    def clean_name(self):
        data = self.cleaned_data['name']

        if len(data) > 100:
            raise ValidationError(_('Invalid Video Name'))

        return data
     
    def clean_url(self):
        video_data = self.cleaned_data['videos']
        #
        return url_data

    def clean_tags(self):
        type_data = self.cleaned_data['types']
        #
        return tag_data
    class Meta:
        model = Tag
        fields = ('name', 'videos', 'types', )
        labels = {
            'name': 'Tag Name',
            'videos': 'Videos',
            'types': 'Categories',
        }


# class AddTypeForm(forms.ModelForm):
#     class Meta:
#         model = Type
#         fields = ('name', )
#         labels = {
#           'name': 'Category',
#         }


class SearchForm(forms.Form):
    query = forms.CharField(label='search videos')
    # https://docs.djangoproject.com/en/dev/topics/forms/
    
