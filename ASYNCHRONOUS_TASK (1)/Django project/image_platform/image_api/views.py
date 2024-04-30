from django.shortcuts import render
import io
from rest_framework import generics
from google.cloud import vision_v1
from google.cloud.vision_v1 import types
from rest_framework import status
from rest_framework.response import Response
from .models import AnalyzedImage, Comment
from .serializers import AnalyzedImageSerializer, CommentSerializer
from rest_framework.pagination import PageNumberPagination

def analyze_image(image_path):
    client = vision_v1.ImageAnnotatorClient()

    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)
    response = client.label_detection(image=image)

    labels = [label.description for label in response.label_annotations]
    return labels

class AnalyzeImageView(generics.CreateAPIView):
    queryset = AnalyzedImage.objects.all()
    serializer_class = AnalyzedImageSerializer

    def perform_create(self, serializer):
        try:
            super().perform_create(serializer)
            image_path = serializer.validated_data['image'].path
            labels = analyze_image(image_path)
            instance = serializer.instance
            instance.description = ', '.join(labels)
            instance.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AnalyzedImageView(generics.RetrieveAPIView):
    queryset = AnalyzedImage.objects.all()
    serializer_class = AnalyzedImageSerializer

class AnalyzedImagesView(generics.ListAPIView):
    queryset = AnalyzedImage.objects.all()
    serializer_class = AnalyzedImageSerializer

class CommentView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    def perform_create(self, serializer):
        super().perform_create(serializer)

        # Get the path to the uploaded image
        image_path = serializer.validated_data['image'].path

        # Analyze the image using Google Cloud Vision API
        labels = analyze_image(image_path)

        # Update the analyzed image instance with labels
        instance = serializer.instance
        instance.description = ', '.join(labels)
        instance.save()
