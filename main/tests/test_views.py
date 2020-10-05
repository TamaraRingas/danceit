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

class VideoDetailViewTest(TestCase): 
  @classmethod
  def setUpTestData(cls):
    video = Video.objects.create(name='TestVideo', url='https:/youtube.com/watch?v=testvideo')
    tag1 = Tag.objects.create(name='test')
    tag2 = Tag.objects.create(name='tag')
    video.tags.add(Tag.objects.get(id=1))
    video.tags.add(Tag.objects.get(id=2))

  def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/main/video/1')
        self.assertEqual(response.status_code, 200)

  def test_view_url_accessible_by_name(self):
      # Use client from TestCase's derived class to simulate a GET request and get a response.
      response = self.client.get(reverse('video-detail', kwargs={'pk': 1}))
      self.assertEqual(response.status_code, 200)

  def test_view_uses_correct_template(self):
        # Use client from TestCase's derived class to simulate a GET request and get a response.
      response = self.client.get(
          reverse('video-detail', kwargs={'pk': 1}))
      self.assertEqual(response.status_code, 200)
      self.assertTemplateUsed(response, 'main/video_detail.html') 

class TagDetailViewTest(TestCase): 
  @classmethod
  def setUpTestData(cls):
    tag = Tag.objects.create(name='test') 
    video = Video.objects.create(name='TestVideo', url='https:/youtube.com/watch?v=testvideo')
    type1 = Type.objects.create(name='Dancer')
    type2 = Type.objects.create(name='Dance Group')
    tag.types.add(Type.objects.get(id=1))
    tag.types.add(Type.objects.get(id=2))

  def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/main/tag/1')
        self.assertEqual(response.status_code, 200)

  def test_view_url_accessible_by_name(self):
      # Use client from TestCase's derived class to simulate a GET request and get a response.
      response = self.client.get(reverse('tag-detail', kwargs={'pk': 1}))
      self.assertEqual(response.status_code, 200)

  def test_view_uses_correct_template(self):
        # Use client from TestCase's derived class to simulate a GET request and get a response.
      response = self.client.get(
          reverse('tag-detail', kwargs={'pk': 1}))
      self.assertEqual(response.status_code, 200)
      self.assertTemplateUsed(response, 'main/tag_detail.html') 

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


class TypeDetailViewTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    type = Type.objects.create(name='Test Category')
    tag1 = Tag.objects.create(name='Dancer')
    tag2 = Tag.objects.create(name='Dance Group')
    type.tags.add(Tag.objects.get(id=1))
    type.tags.add(Tag.objects.get(id=2))

  def test_view_url_exists_at_desired_location(self):
      response = self.client.get('/main/category/1')
      self.assertEqual(response.status_code, 200)

  def test_view_url_accessible_by_name(self):
      # Use client from TestCase's derived class to simulate a GET request and get a response.
      response = self.client.get(reverse('type-detail', kwargs={'pk': 1}))
      self.assertEqual(response.status_code, 200)

  def test_view_uses_correct_template(self):
      # Use client from TestCase's derived class to simulate a GET request and get a response.
      response = self.client.get(
          reverse('type-detail', kwargs={'pk': 1}))
      self.assertEqual(response.status_code, 200)
      self.assertTemplateUsed(response, 'main/type_detail.html')

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
    tag_objects_for_video = Tag.objects.all()
    test_video.tags.set(tag_objects_for_video) # Direct assignment of many-to-many types not allowed. 
    test_video.save()

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('my-videos')) #Try to access in to the my-videos page
        self.assertRedirects(
            response, '/accounts/login/?next=/main/myvideos/') #Check if it redirects user that aren't logged in.

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(
            username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('my-videos'))
        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        # Check we used correct display template
        self.assertTemplateUsed(
            response, 'main/videos_by_user.html')

    def test_only_saved_videoss_in_list(self):
        login = self.client.login(
            username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('my-videos'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        # Check that initially we don't have any videos in list 
        self.assertTrue('video_list' in response.context)
        self.assertEqual(len(response.context['video_list']), 0)

        videos = Video.objects,all()[:10]

        for video in videos:
          video.user = test_user1
          video.save()

        # Check that now we have saved videos in the list
        response = self.client.get(reverse('my-videos'))
        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        self.assertTrue('video_list' in response.context)

        # Confirm all videos belong to testuser1
        for video in response.context['video_list']:
            self.assertEqual(response.context['user'], video.user)
            

class UserTagsListViewTest(TestCase):
  def setUp(self):
    test_user1 = User.objects.create_user(
        username='testuser1', password='1X<ISRUkw+tuK')
    test_user2 = User.objects.create_user(
        username='testuser2', password='2HJ1vRV0Z&3iD')
    test_user1.save()
    test_user2.save()

    test_type = Type.objects.create(name='Dance Group')
    test_tag = Tag.objects.create(name='Masaka Kids', type=test_type)
    test_video = Video.objects.create(
        name='Masaka Kids Africana Dancing Koti Ko', url='https://www.youtube.com/watch?v=_ynkzpwUEMQ', tags=test_tag, usser=test_user1)
    
    #Create videos as a post-step
    video_objects_for_tag = Video.objects.all()
    # Direct assignment of many-to-many types not allowed.
    test_tag.videos.set(video_objects_for_tag)
    test_tag.save()

    #Create additional types as a post-step
    type_objects_for_tag = Type.objects.all()
    # Direct assignment of many-to-many types not allowed.
    test_tag.types.set(type_objects_for_tag)
    test_tag.save()

    def test_redirect_if_not_logged_in(self):
        # Try to access in to the my-tags page
        response = self.client.get(reverse('my-tags'))
        self.assertRedirects(
            response, '/accounts/login/?next=/main/mytags/')  # Check if it redirects users that aren't logged in.

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(
            username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('my-videos'))
        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        # Check we used correct display template
        self.assertTemplateUsed(
            response, 'main/tags_by_user.html')

    def test_only_saved_videoss_in_list(self):
        login = self.client.login(
            username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('my-tags'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        # Check that initially we don't have any tags in list
        self.assertTrue('tag_list' in response.context)
        self.assertEqual(len(response.context['tag_list']), 0)

        tags = Tag.objects, all()[:10]

        for tag in tags:
          tag.user = test_user1
          tag.save()

        # Check that now we have saved videos in the list
        response = self.client.get(reverse('my-tags'))
        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        self.assertTrue('tag_list' in response.context)

        # Confirm all tags displayed belong to testuser1
        for tag in response.context['tag_list']:
            self.assertEqual(response.context['user'], tag.user)
    
