from django.test import TestCase
from .models import Tag, Video, Type

class TagModelTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    # Set up non-modified objects used by all test methods
    Tag.objects.create(name='Balanata')

  def test_tag_name(self):
    tag = Tag.objects.get(id=1)
    field_label = tag._meta.get_field('name').verbose_name
    self.assertEquals(field_label, 'name')


class TypeModelTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    # Set up non-modified objects used by all test methods
    Type.objects.create(name='Dance Group')

  def test_type_name(self):
    type = Type.objects.get(id=1)
    field_label = type._meta.get_field('name').verbose_name
    self.assertEquals(field_label, 'name')


class VideoModelTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    # Set up non-modified objects used by all test methods
    Video.objects.create(name='Agbadza dance Volta region of Ghana')
    Video.objects.create(url='https://youtu.be/fQNMMI81OEk')

  def test_video_name(self):
    video = Video.objects.get(id=1)
    field_label = video._meta.get_field('name').verbose_name
    self.assertEquals(field_label, 'name')

  def test_video_url(self):
    video = Video.objects.get(id=1)
    field_label = video._meta.get_field('url').verbose_name
    self.assertEquals(field_label, 'url')
