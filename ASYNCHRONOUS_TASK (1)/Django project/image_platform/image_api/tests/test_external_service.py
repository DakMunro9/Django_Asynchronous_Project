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
        labels = analyze_image("C:\Users\ADMIN\OneDrive\Desktop\Django project\image_platform\2023-07-29_11.jpg")

        # Check if the function processes the external service's response correctly
        self.assertEqual(labels, ["Label1", "Label2"])
