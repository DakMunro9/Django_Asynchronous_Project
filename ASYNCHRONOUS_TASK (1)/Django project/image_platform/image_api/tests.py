from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from image_api.models import AnalyzedImage

class AnalyzeImageViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_analyze_image(self):
        # Create a dummy image file for testing
        image_path = "C:/Users/ADMIN/OneDrive/Desktop/Django project/image_platform/2023-07-29_11.jpg"
        with open(image_path, "rb") as image_file:
            response = self.client.post(
                "/api/analyze-image/",
                data={"image": image_file},
                format="multipart",
            )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class AnalyzedImagesViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_retrieve_analyzed_images(self):
        response = self.client.get("/api/images/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
from django.test import TestCase
from image_api.models import AnalyzedImage, Comment

class AnalyzedImageModelTest(TestCase):
    def test_analyzed_image_str(self):
        image = AnalyzedImage.objects.create(description="Test Image")
        self.assertEqual(str(image), "Test Image")

class CommentModelTest(TestCase):
    def test_comment_str(self):
        image = AnalyzedImage.objects.create(description="Test Image")
        comment = Comment.objects.create(image=image, text="Test Comment")
        self.assertEqual(str(comment), "Test Comment")

from django.test import TestCase
from unittest.mock import patch
from image_api.views import analyze_image

class ExternalServiceIntegrationTest(TestCase):
    @patch("image_api.views.vision_v1.ImageAnnotatorClient")
    def test_analyze_image_with_external_service(self, mock_client):
        # Mock the external service's response
        mock_response = mock_client.return_value
        mock_response.label_detection.return_value = [
            {"description": "Label1"},
            {"description": "Label2"},
        ]

        # Call the function that integrates with the external service
        labels = analyze_image("C:/Users/ADMIN/OneDrive/Desktop/Django project/image_platform/2023-07-29_11.jpg")

        # Check if the function processes the external service's response correctly
        self.assertEqual(labels, ["Label1", "Label2"])
