from django.db import models
from django.urls import reverse
from django.utils import timezone 
from django.contrib.auth.models import User
class Video(models.Model):
  """Represents a Youtube video uploaded to our database, derived from the Model class."""

  name = models.CharField(max_length=100)
  url = models.URLField()
  #date_created = models.DateTimeField(default=timezone.now) 
  """Local time used because users will be all over the world"""
  # search = models.CharField(max_length=20, null=True, blank=True) 
  tags = models.ManyToManyField("Tag", blank=True)
  user = models.ForeignKey(
      User, on_delete=models.SET_NULL, null=True, blank=True)

  class Meta:
      ordering = ['name']

  def get_absolute_url(self):
    """Returns the url to access a particular instance of Video."""
    return reverse('video-detail', args=[str(self.id)])

  def make_embed_url(self):
    return self.url + 'some text'

  def __str__(self):
    """String representation of the Video object."""
    return self.name

class Tag(models.Model):
  """Represents a Video Tag, derived from the Model class."""

  name = models.CharField(max_length=20)
  #date_created = models.DateTimeField(default=timezone.now)

  videos = models.ManyToManyField(Video)
  types = models.ManyToManyField("Type")
  user = models.ForeignKey(
      User, on_delete=models.SET_NULL, null=True, blank=True)
  
  class Meta:
      ordering = ['name']

  def get_absolute_url(self):
    """Returns the url to access a particular Tag."""
    return reverse('tag-detail', args=[str(self.id)])

  def __str__(self):
    """String representation of the Tag object."""
    return self.name

class Type(models.Model):
  """ Categories of Tags """
  name = models.CharField(max_length=20)

  tags = models.ManyToManyField(Tag)

  class Meta:
      ordering = ['name']

  def get_absolute_url(self):
    """Returns the url to access a particular Tag."""
    return reverse('type-detail', args=[str(self.id)])

  def __str__(self):
    """String representation of the Type object."""
    return self.name
  
