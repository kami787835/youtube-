from django.urls import path
from .views import VideoListView, VideoDetail, CommentDetail,  VideoViewed ,VideoLiked

urlpatterns = [
    path('videos/', VideoListView.as_view(), name='video-list'),
    path('videos/<int:pk>/', VideoDetail.as_view(), name='video-detail'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),
    path('videos/<int:pk>/просмотр/', VideoViewed.as_view(), name='video-viewed'),
    path('videos/<int:pk>/like/', VideoLiked.as_view(), name='video-liked'),

]