from django import forms
from django.forms import ModelForm
from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import requests
from main.models import Video, Tag, Type


class AddVideoForm(ModelForm):

    def clean_name(self):  # Override clean_data method from ModelForm class.
        data = self.cleaned_data['name']

        if len(data) > 100:  # Check that name entered is valid.
            # If not, raise error.
            raise ValidationError(_('Invalid Video Name'))

        return data

    # Override clean_data method for the data in each field.
    def clean_url(self):
        url_data = self.cleaned_data['url']
        #
        return url_data

    def clean_tags(self):
        tag_data = self.cleaned_data['tags']
        #
        return tag_data

    class Meta:
        model = Video  # Set model class.
        # List which fields are used in form.
        fields = ['name', 'url', 'tags', ]
        labels = {  # Set field labels
            'name': 'Video Name',
            'url': 'Video URL',
            'tags': 'Tags',
        }


class AddTagForm(forms.ModelForm):
    def clean_name(self):  # Override clean_data method from ModelForm class.
        data = self.cleaned_data['name']

        if len(data) > 100:  # Check form validity.
            raise ValidationError(_('Invalid Tag Name'))

        return data

    def clean_url(self):
        video_data = self.cleaned_data['videos']
        #
        return video_data

    def clean_tags(self):
        type_data = self.cleaned_data['types']

        return type_data

    class Meta:  # Set fields and labels.
        model = Tag
        fields = ('name', 'videos', 'types', )
        labels = {
            'name': 'Tag Name',
            'videos': 'Videos',
            'types': 'Categories',
        }


class AddTypeForm(forms.ModelForm):
    def clean_name(self):
        data = self.cleaned_data['name']
        return data

    def clean_tags(self):
        tag_data = self.cleaned_data['tags']
        return tag_data

    class Meta:
        model = Type
        fields = ('name', 'tags', )
        labels = {
            'name': 'Category',
            'tags': 'Tags',
        }
