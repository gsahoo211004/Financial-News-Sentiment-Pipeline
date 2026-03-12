from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=500)
    url = models.URLField(unique=True)
    published_at = models.DateTimeField()
    sentiment_score = models.FloatField()
    sentiment_label = models.CharField(max_length=20)
    summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title