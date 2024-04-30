
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from image_api.models import AnalyzedImage

class AnalyzeImageViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_analyze_image(self):
        # Create a dummy image file for testing
        image_path = "path/to/your/test/image.jpg"
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