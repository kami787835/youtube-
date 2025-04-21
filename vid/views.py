from django.http import Http404
from rest_framework import generics
from .models import Video,Comment
from .serializers import VideoSerializer,CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from .filters import VideoFilter

class VideoListView(ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title']
    search_fields = ['title']
    filters =VideoFilter
class VideoDetail(generics.RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class CommentDetail(APIView):
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)


class VideoViewed(APIView):
    def post(self, request, pk):
        video = generics.get_object_or_404(Video, pk=pk)
        video.views += 1
        video.save()
        serializer = VideoSerializer(video)
        return Response({'views': serializer.data['views']})

class VideoLiked(APIView):
    def post(self, request, pk):
        video = generics.get_object_or_404(Video, pk=pk)
        video.likes += 1
        video.save()
        serializer = VideoSerializer(video)
        return Response({'likes': serializer.data['likes']})
