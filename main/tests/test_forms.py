from django.test import TestCase
from main.forms import *

class AddVideoFormTest(TestCase):
  def test_add_video_form_name_field(self):
    form = AddVideoForm()
    self.assertTrue(form.fields['name'].label ==
                    None or form.fields['name'].label == 'Video Name')

  def test_add_video_form_url_field(self):
    form = AddVideoForm()
    self.assertTrue(form.fields['url'].label ==
                    None or form.fields['url'].label == 'Video URL')

