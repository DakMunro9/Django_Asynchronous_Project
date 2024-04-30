# image_api/models.py

from django.db import models

class AnalyzedImage(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return f"AnalyzedImage #{self.id}"

class Comment(models.Model):
    image = models.ForeignKey(AnalyzedImage, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"Comment #{self.id} for AnalyzedImage #{self.image.id}"
