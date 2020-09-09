from django import forms

class AddVideoForm(forms.Form):
  video_name = forms.CharField()
  url = forms.CharField()