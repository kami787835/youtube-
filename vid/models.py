from django.db import models
class Video(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    file = models.FileField(upload_to='videos/')
class Comment(models.Model):
    video = models.ForeignKey(Video, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()