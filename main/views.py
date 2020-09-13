from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse 
from django.urls import reverse_lazy
from main.models import Video, Tag, Type
from main.forms import AddVideoForm 
from .filters import VideoFilter

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

# def add_video(request, pk):
#   video = get_object_or_404(Video, pk=pk)

#   if request.method == "POST":
#     # Create a form instance and populate it with data from the request (binding)
#     form = AddVideoForm(request.POST)
#     if form.is_valid():
      

class VideoListView(generic.ListView):
    model = Video
    paginate_by = 10
    myFilter = VideoFilter()

class VideoDetailView(generic.DetailView):
    model = Video

class TagListView(generic.ListView):
  model = Tag
  paginate_by = 10

class TagDetailView(generic.DetailView):
  model = Tag

class TypeListView(generic.ListView):
  model = Type 

class TypeDetailView(generic.DetailView):
  model = Type

class VideoCreate(CreateView):
  model = Video
  fields = '__all__'

class VideoUpdate(UpdateView):
  model = Video
  fields = '__all__'

class VideoDelete(DeleteView):
  model = Video
  success_url = reverse_lazy('videos')

class TagCreate(CreateView):
  model = Tag
  fields = '__all__'

class TagUpdate(UpdateView):
  model = Tag 
  fields = '__all__'

class TagDelete(DeleteView):
  model = Tag
  success_url = reverse_lazy('tags')
