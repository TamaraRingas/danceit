from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('videos/', views.VideoListView.as_view(), name='videos'),
    path('video/<int:pk>', views.VideoDetailView.as_view(), name='video-detail'),
    path('tags/', views.TagListView.as_view(), name='tags'),
    path('tag/<int:pk>', views.TagDetailView.as_view(), name='tag-detail'),
    path('accounts/', include('django.contrib.auth.urls')),
]
