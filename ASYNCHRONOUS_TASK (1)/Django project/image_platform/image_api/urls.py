# urls.py

from django.urls import path
from .views import AnalyzeImageView, AnalyzedImagesView, AnalyzedImageView, CommentView

urlpatterns = [
    path('analyze-image/', AnalyzeImageView.as_view(), name='analyze-image'),
    path('images/', AnalyzedImagesView.as_view(), name='images'),
    path('image/<int:pk>/', AnalyzedImageView.as_view(), name='image-detail'),
    path('image/<int:pk>/comment/', CommentView.as_view(), name='add-comment'),
]