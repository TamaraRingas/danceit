from django.shortcuts import render
from main.models import Video, Tag

def index(request):
  num_videos = Video.objects.all().count()
  num_tags = Tag.objects.all().count()

  context = {
    'num_videos': num_videos,
    'num_tags': num_tags,
  }

  return render(request, 'index.html', context=context)
