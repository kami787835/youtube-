from rest_framework import serializers
from .models import Video, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text']

class VideoSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Video
        fields = ['id', 'title', 'url', 'comments','views','likes','file']
