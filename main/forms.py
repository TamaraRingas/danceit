from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from main.models import Video, Tag, Type


class AddVideoForm(forms.ModelForm):
    name = forms.CharField(required=True)
    url = forms.URLField(required=True)
    class Meta:
        model = Video
        fields = ('name', 'url', 'tags', )
        labels = {
            'name': 'Video Name',
            'url': 'Video URL',
            'tags': 'Tags',
        }

    def clean_name(self):
      data = self.cleaned_data['name']

      


# class AddTagFrom(forms.ModelForm):
#     class Meta:
#         model = Tag
#         fields = ('name', 'videos', 'types', )
#         labels = {
#             'name': 'Tag Name',
#             'videos': 'Videos',
#             'types': 'Categories',
#         }


# class AddTypeForm(forms.ModelForm):
#     class Meta:
#         model = Type
#         fields = ('name', )
#         labels = {
#           'name': 'Category',
#         }
