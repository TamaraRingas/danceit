from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.conf import settings
from django.urls import reverse 
from django.urls import reverse_lazy
from main.models import Video, Tag, Type
from main.forms import AddVideoForm
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from isodate import parse_duration
import requests 

def index(request):
  videos = Video.objects.all()
  # recent_videos = Video.objects.all().order_by(-'date_created')
  recent_videos = videos[:4]
  num_videos = Video.objects.all().count()
  num_tags = Tag.objects.all().count()

  """Number of visits to this view, as counted in the session variable.
     This will be used in final system to get users favourite videos """
  num_visits = request.session.get('num_visits', 0)
  request.session['num_visits'] = num_visits + 1

  context = {
    'videos': videos,
    'num_videos': num_videos,
    'num_tags': num_tags,
    'num_visits': num_visits,
    'recent_videos': recent_videos,
  }

  return render(request, 'index.html', context=context)

def video_search(request, query):
  form = SearchForm(request.GET)
  query = request.GET['query']
  search_results = Video.objects.filter(name__icontains=query)

  context = {
    'search_results': search_results
  }

  return render(request, 'main/video_list.html', context=context)

def search_youtube(request): #View methods for searching videos through YouTube API. 
  youtubevideos = []
  if request.method == 'POST': 
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    video_url = 'https://www.googleapis.com/youtube/v3/videos'
    search_params = {
      'part': 'snippet',
      'q': request.POST['search'],
      'key': settings.YOUTUBE_DATA_API_KEY,
      'type': 'video',
      'maxResults': 6
    }
    video_ids = []
    r = requests.get(search_url, params=search_params)
    results = r.json()['items']
    for result in results:
      video_ids.append(result['id']['videoId'])
    
    video_params = {
      'key': settings.YOUTUBE_DATA_API_KEY,
      'part': 'snippet, contentDetails',
      'id': ','.join(video_ids),
    }
    r = requests.get(video_url, params=video_params)

    results = r.json()['items']
    
    for result in results:
      video_data = {
          'title': result['snippet']['title'],
          'id': result['id'],
          'url': f'https://www.youtube.com/watch?v={result["id"]}',
          'duration': parse_duration(result['contentDetails']['duration']),
          'thumbnail': result['snippet']['thumbnails']['high']['url'],
          'maxResults': 6
      }
      youtubevideos.append(video_data)
  context = {
      'youtubevideos': youtubevideos
  }
  return render(request, 'index.html', context)

def signup_view(request): #View method to use signup form and display it to the user.
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('index')
    return render(request, 'signup.html', {'form': form})

class VideoListView(generic.ListView): # View class that gets and displays video list.
                                       # Inherited from the ListView Class
    model = Video
    paginate_by = 10

    def get_queryset(self):
      query = self.request.GET.get('query', None)

      if query:
        return Video.objects.filter(name__icontains=query)

      else:
        return Video.objects.all()
    
    

class VideoDetailView(generic.DetailView): # View class that displays Video Details. 
                                           # Extended from the DetailView class.
    model = Video

class TagListView(generic.ListView): # View class that displays list of Tags. 
                                       # Extended from the ListView class.
  model = Tag
  paginate_by = 10

  def get_queryset(self):
      query = self.request.GET.get('query', None)

      if query:
        return Tag.objects.filter(name__icontains=query)

      else:
        return Tag.objects.all()

   model = Tag

class TypeListView(generic.ListView): # View class that displays list of Tag Categories. 
                                      # Extended from the ListView class.
  model = Type 

  def get_queryset(self):
      query = self.request.GET.get('query', None)

      if query:
        return Type.objects.filter(name__icontains=query)

      else:
        return Type.objects.all()

class TypeDetailView(generic.DetailView): # View class that displays Tag Category Details. 
                                          # Extended from the DetailView class.
  model = Type

class VideoCreate(CreateView): #View class to display VideoCreate Form, extended from CreateView class.
  model = Video
  fields = '__all__'

class VideoUpdate(UpdateView): #View class to display VideoUpdate Form, extended from UpdateView class.
  model = Video
  fields = '__all__'

class VideoDelete(DeleteView): #View class to display VideoDelete Form, extended from DeleteView class.
  model = Video
  success_url = reverse_lazy('videos')

class TagCreate(CreateView): #View class to display TagCreate Form, extended from CreateView class.
  model = Tag
  fields = '__all__'

class TagUpdate(UpdateView): #View class to display TagUpdate Form, extended from UpdateView class.
  model = Tag 
  fields = '__all__'

class TagDelete(DeleteView): #View class to display TagDelete Form, extended from DeleteView class.
  model = Tag
  success_url = reverse_lazy('tags')

class TypeCreate(CreateView): #View class to display TypeCreate Form, extended from CreateView class.
  model = Type
  fields = '__all__'

class UserVideosListView(LoginRequiredMixin, generic.ListView): # View class to display users VideoList, extended from ListView
  model = Video
  template_name = 'main/videos_by_user.html'
  paginate_by = 20

  def get_queryset(self):
      return Video.objects.filter(user=self.request.user)


class UserTagsListView(LoginRequiredMixin, generic.ListView): # View class to display users TagList, extended from ListView
  model = Tag
  template_name = 'main/tags_by_user.html'
  paginate_by = 20

  def get_queryset(self):
      return Tag.objects.filter(user=self.request.user)

