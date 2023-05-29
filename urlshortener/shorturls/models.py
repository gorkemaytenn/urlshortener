from django.db import models


class URL(models.Model):
    original_url = models.URLField('Original URL', blank=False)
    shortened_url = models.CharField(
        'Shortened URL', unique=True, blank=False)
    created_at = models.DateTimeField('Createt At', auto_now_add=True)
    times_followed = models.IntegerField(default=0)
    last_accessed = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.original_url
