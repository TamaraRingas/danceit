from django.contrib import admin
from .models import Video, Tag, Type

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
  pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
  pass

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
  pass

