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

  def test_add_video_form_url_field(self):
    form = AddVideoForm()
    self.assertTrue(form.fields['url'].label ==
                    None or form.fields['url'].label == 'Video URL')


class AddTagFormTest(TestCase):
  def test_add_tag_form_name_field(self):
    form = AddTagForm()
    self.assertTrue(form.fields['name'].label ==
                    None or form.fields['name'].label == 'Tag Name')

  def test_add_tag_form_videos_field(self):
    form = AddTagForm()
    self.assertTrue(form.fields['videos'].label ==
                    None or form.fields['videos'].label == 'Videos')

  def test_add_video_form_url_field(self):
    form = AddTagForm()
    self.assertTrue(form.fields['types'].label ==
                    None or form.fields['types'].label == 'Categories')


class AddTypeFormTest(TestCase):
  def test_add_type_form_name_field(self):
    form = AddTypeForm()
    self.assertTrue(form.fields['name'].label ==
                    None or form.fields['name'].label == 'Category')

  def test_add_tag_form_tags_field(self):
    form = AddTypeForm()
    self.assertTrue(form.fields['tags'].label ==
                    None or form.fields['tags'].label == 'Tags')
