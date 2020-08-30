from django.contrib import admin
from .models import Video, Tag

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
  pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
  pass

