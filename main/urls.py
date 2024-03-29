from django.urls import path
from . import views
#Map URLS with their Views. 
urlpatterns = [ 
    path('', views.search_youtube, name='index'),
    path('videos/', views.VideoListView.as_view(), name='videos'),
    path('video/<int:pk>', views.VideoDetailView.as_view(), name='video-detail'),
    path('youtube', views.search_youtube, name='youtube_search'),
    path('tags/', views.TagListView.as_view(), name='tags'),
    path('tag/<int:pk>', views.TagDetailView.as_view(), name='tag-detail'),
    path('Tag Categories/', views.TypeListView.as_view(), name = 'types'),
    path('category/<int:pk>', views.TypeDetailView.as_view(), name='type-detail'),
    path('video/create/', views.VideoCreate.as_view(), name='video_create'),
    path('video/<int:pk>/share/', views.VideoShare.as_view(), name='video_share'),
    path('video/<int:pk>/update/',
         views.VideoUpdate.as_view(), name='video_update'),
    path('video/<int:pk>/delete/',
         views.VideoDelete.as_view(), name='video_delete'),
    path('tag/create/', views.TagCreate.as_view(), name='tag_create'),
    path('category/create/', views.TypeCreate.as_view(), name='type_create'),
    path('tag/<int:pk>/update/',
         views.TagUpdate.as_view(), name='tag_update'),
    path('tag/<int:pk>/share/', views.TagShare.as_view(), name='tag_share'),
    path('tag/<int:pk>/delete/',
         views.TagDelete.as_view(), name='tag_delete'),
    path('myvideos/', views.UserVideosListView.as_view(), name='my-videos'),
    path('mytags/', views.UserTagsListView.as_view(), name='my-tags'),
    path('signup/', views.signup_view, name="signup"),
    path('faq/', views.faq_view, name='faq'),
    
]


