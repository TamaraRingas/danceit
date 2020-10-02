from django.test import TestCase
from django.urls import reverse
from main.models import Video, Tag, Type

class VideoListViewTest(TestCase):
  @classmethod
  def setUpTestData(cls):
      # Create 21 videos for pagination tests
      number_of_videos = 21

      for video_id in range(number_of_videos):
        Video.objects.create(
          name=f'TestVideo {video_id}'
        )
      
  def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/main/videos/')
        self.assertEqual(response.status_code, 200)

  def test_view_url_accessible_by_name(self):
    response = self.client.get(reverse('videos'))
    self.assertEqual(response.status_code, 200)
