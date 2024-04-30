from django.test import TestCase
from image_api.models import AnalyzedImage, Comment

class AnalyzedImageModelTest(TestCase):
    def test_analyzed_image_str(self):
        image = AnalyzedImage.objects.create(description="Test Image")
        self.assertEqual(str(image), "Test Image")

class CommentModelTest(TestCase):
    def test_comment_str(self):
        comment = Comment.objects.create(text="Test Comment")
        self.assertEqual(str(comment), "Test Comment")