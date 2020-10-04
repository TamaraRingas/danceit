from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.models import Permission, User
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

    def test_lists_all_videos(self):
        # Get second page and confirm it has (exactly) 3 remaining items
        response = self.client.get(reverse('videos')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['video_list']) == 3)


class TagListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 tags.
        number_of_tags = 13

        for tag_id in range(number_of_tags):
            Video.objects.create(
                name=f'TestTag {tag_id}'
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/main/tags/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        # Use client from TestCase's derived class to simulate a GET request and get a response.
        response = self.client.get(reverse('tags'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        # Use client from TestCase's derived class to simulate a GET request and get a response.
        response = self.client.get(reverse('tags'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/tag_list.html')


class TypeListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13  categories.
        number_of_types = 3

        for type_id in range(number_of_types):
            Video.objects.create(
                name=f'TestType {type_id}'
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/main/Tag Categories/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        # Use client from TestCase's derived class to simulate a GET request and get a response.
        response = self.client.get(reverse('types'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        # Use client from TestCase's derived class to simulate a GET request and get a response.
        response = self.client.get(reverse('types'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/type_list.html')


class UserVideosListViewTest(TestCase):
  def setUp(self):
    test_user1 = User.objects.create_user(
        username='testuser1', password='1X<ISRUkw+tuK')
    test_user2 = User.objects.create_user(
        username='testuser2', password='2HJ1vRV0Z&3iD')
    test_user1.save()
    test_user2.save()

    test_type = Type.objects.create(name='Dance Group')
    test_tag = Tag.objects.create(name='Masaka Kids',type=test_type)
    test_video = Video.objects.create(
        name='Masaka Kids Africana Dancing Koti Ko', url='https://www.youtube.com/watch?v=_ynkzpwUEMQ',tags=test_tag,usser=test_user1)

    #Create tags as a post-step
    tag_objects_for_video - Tag.objects.all()
    test_video.tags.set(tag_objects_for_video) # Direct assignment of many-to-many types not allowed. 
    test_video.save()

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('my-videos'))
        self.assertRedirects(
            response, '/accounts/login/?next=/catalog/myvideo/')

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(
            username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('my-videos'))
        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        # Check we used correct template
        self.assertTemplateUsed(
            response, 'main/videos_by_user.html')

    
