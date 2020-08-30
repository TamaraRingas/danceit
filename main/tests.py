from django.test import TestCase
from .models import Tag 

class TagModelTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    # Set up non-modified objects used by all test methods
    Tag.objects.create(name='Balanata')

  def test_tag_name(self):
    tag = Tag.objects.get(id=1)
    field_label = tag._meta.get_field('name').verbose_name
    self.assertEquals(field_label, 'name')

