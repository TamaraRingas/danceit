from django.test import TestCase
from main.models import Tag, Video, Type

class TagModelTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    # Set up non-modified objects used by all test methods
    Tag.objects.create(name='Balanata')
    Tag.objects.create(name='Dance')
    Type.objects.create(name='Location')
    Type.objects.create(name='Dance Style')
    
  def test_tag_name(self):
    tag = Tag.objects.get(id=1)
    field_label = tag._meta.get_field('name').verbose_name
    self.assertEquals(field_label, 'name')

  def test_name_max_length(self):
      tag = Tag.objects.get(id=1)
      max_length = tag._meta.get_field('name').max_length
      self.assertEquals(max_length, 20)

  def test_tag_types(self):
    tag = Tag.objects.get(id=1)
    tag.types.add(Type.objects.get(id=1))
    tag.types.add(Type.objects.get(id=2))
    count = Type.objects.count()
    self.assertEquals(count, 2)

  def test_get_absolute_url(self):
      tag = Tag.objects.get(id=1)
      # This will also fail if the urlconf is not defined.
      self.assertEquals(tag.get_absolute_url(), '/main/tag/1')

class TypeModelTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    # Set up non-modified objects used by all test methods
    Type.objects.create(name='Dance Group')
    Tag.objects.create(name='Performers')
    Tag.objects.create(name='Dancers')

  def test_type_name(self):
    type = Type.objects.get(id=1)
    field_label = type._meta.get_field('name').verbose_name
    self.assertEquals(field_label, 'name')

  def test_name_max_length(self):
      type = Type.objects.get(id=1)
      max_length = type._meta.get_field('name').max_length
      self.assertEquals(max_length, 20)

  def test_type_tags(self):
    type = Type.objects.get(id=1)
    type.tags.add(Tag.objects.get(id=1))
    type.tags.add(Tag.objects.get(id=2))
    count = Tag.objects.count()
    self.assertEquals(count, 2)

  def test_get_absolute_url(self):
      type = Type.objects.get(id=1)
      # This will also fail if the urlconf is not defined.
      self.assertEquals(type.get_absolute_url(), '/main/category/1')


class VideoModelTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    # Set up non-modified objects used by all test methods
    Video.objects.create(name='Agbadza dance Volta region of Ghana')
    Video.objects.create(url='https://youtu.be/fQNMMI81OEk')
    Tag.objects.create(name='Dance')
    Tag.objects.create(name='Tutorial')
    
  def test_video_name(self):
    video = Video.objects.get(id=1)
    field_label = video._meta.get_field('name').verbose_name
    self.assertEquals(field_label, 'name')

  def test_video_url(self):
    video = Video.objects.get(id=1)
    field_label = video._meta.get_field('url').verbose_name
    self.assertEquals(field_label, 'url')

  def test_video_tags(self):
    video = Video.objects.get(id=1)
    video.tags.add(Tag.objects.get(id=1))
    video.tags.add(Tag.objects.get(id=2))
    count = Tag.objects.count()
    self.assertEquals(count, 2)

  def test_name_max_length(self):
      video = Video.objects.get(id=1)
      max_length = video._meta.get_field('name').max_length
      self.assertEquals(max_length, 100)
 
  def test_get_absolute_url(self):
      video = Video.objects.get(id=1)
      # This will also fail if the urlconf is not defined.
      self.assertEquals(video.get_absolute_url(), '/main/video/1')
