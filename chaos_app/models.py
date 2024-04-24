from django.db import models

class Image(models.Model):
    prompt = models.CharField(max_length=255)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    