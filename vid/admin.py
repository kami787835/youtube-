from django.contrib import admin
from .models import Video, Comment

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('video', 'text')