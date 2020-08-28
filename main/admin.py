from django.contrib import admin
from .models import Video, Tag

 class VideoAdmin(admin.ModelAdmin):
   pass

admin.site.register(Video, VideoAdmin)

class TagAdmin(admin.ModelAdmin):
  pass

admin.site.register(Tag, TagAdmin)
