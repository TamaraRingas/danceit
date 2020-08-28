ddfrom django.db import models
from django.urls import reverse

class Video(models.Model):
ed  """Represents a Youtube video uploaded to our database, derived from the Model class."""

  name = models.CharField(max_length=100)
  url = models.CharField(max_length=100)
  date_created = models.DateTimeField()

  #tag = models.ManyToManyField("Tag")

  class Meta:
      ordering = ['name']

  def get_absolute_url(self):
    """Returns the url to access a particular instance of Video."""
    return reverse('video-detail-view', args=[str(self.id)])

  def __str__(self):
    """String representation of the Video object."""
    return self.name

class Tag(models.Model):
  """Represents a Video Tag, derived from the Model class."""

  name = models.CharField(max_length=20)
  date_created = models.DateTimeField()

  #video = models.ManyToManyField(Video)
  class Meta:
      ordering = ['name']

  def get_absolute_url(self):
    """Returns the url to access a particular Tag."""
    return reverse('tag-detail-view', args=[str(self.id)])

  def __str__(self):
    """String representation of the Tag object."""
    return self.name


