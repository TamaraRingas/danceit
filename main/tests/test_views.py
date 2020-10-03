from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin 
from main.models import Video, Tag, Type


class VideoListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 videos for pagination tests
        number_of_videos = 13

        for video_id in range(number_of_videos):
            Video.objects.create(
                name=f'TestVideo {video_id}'
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/main/videos/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        # Use client from TestCase's derived class to simulate a GET request and get a response.
        response = self.client.get(reverse('videos'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        # Use client from TestCase's derived class to simulate a GET request and get a response.
        response = self.client.get(reverse('videos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/video_list.html')

    def test_pagination_is_ten(self):
        response = self.client.get(reverse('videos'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context) #Conext var passed to template by the view.
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['video_list']) == 10)

    def test_lists_all_authors(self):
        # Get second page and confirm it has (exactly) 3 remaining items
        response = self.client.get(reverse('videos')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['video_list']) == 3)
