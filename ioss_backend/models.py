from django.db import models

class ShortenedURL(models.Model):
    original_url = models.URLField(max_length=2048)
    short_code = models.CharField(max_length=8, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    click_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"
