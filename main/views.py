from django.shortcuts import render
from django.views import generic
from main.models import Video, Tag

def index(request):
  num_videos = Video.objects.all().count()
  num_tags = Tag.objects.all().count()

  """Number of visits to this view, as counted in the session variable.
     This will be used in final system to get users favourite videos """
  num_visits = request.session.get('num_visits', 0)
  request.session['num_visits'] = num_visits + 1

  context = {
    'num_videos': num_videos,
    'num_tags': num_tags,
    'num_visits': num_visits,
  }

  return render(request, 'index.html', context=context)

class VideoListView(generic.ListView):
    model = Video
    paginate_by = 10

class VideoDetailView(generic.DetailView):
    model = Video

class TagListView(generic.ListView):
  model = Tag
  paginate_by = 10

class TagDetailView(generic.DetailView):
  model = Tag
