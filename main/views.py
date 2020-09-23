from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse 
from django.urls import reverse_lazy
from main.models import Video, Tag, Type
from main.forms import AddVideoForm, SearchForm 
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def index(request):
  videos = Video.objects.all()
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

def signup_view(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('index')
    return render(request, 'signup.html', {'form': form})

class VideoListView(generic.ListView):
    model = Video
    paginate_by = 10

    def get_queryset(self):
      query = self.request.GET.get('query', None)

      if query:
        return Video.objects.filter(name__icontains=query)

      else:
        return Video.objects.all()
    
    

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

class TypeCreate(CreateView):
  model = Type
  fields = '__all__'

class UserVideosListView(LoginRequiredMixin, generic.ListView):
  model = Video
  template_name = 'main/videos_by_user.html'
  paginate_by = 20

  def get_queryset(self):
      return Video.objects.filter(user=self.request.user)


class UserTagsListView(LoginRequiredMixin, generic.ListView):
  model = Tag
  template_name = 'main/tags_by_user.html'
  paginate_by = 20

  def get_queryset(self):
      return Tag.objects.filter(user=self.request.user)
