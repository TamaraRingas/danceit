from django.db import models
from django.urls import reverse

class Video(models.Model):
  """Represents a Youtube video uploaded to our database."""

  name = models.CharField(max_length=100)
  url = models.CharField(max_length=100)

  def get_absolute_url(self):
    """Returns the url to access a particular instance of Video."""
    return reverse('video-detail-view', args=[str(self.id)])

  def __str__(self):
    """String representation of the Video object."""
    return self.name