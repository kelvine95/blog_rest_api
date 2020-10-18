from django.db import models

from organizer.models import Tag, Startup

class Post(models.Model):
    """Blog post; news article about startups"""
    title = models.CharField(max_length = 63)
    slug = models.SlugField(max_length=63)
    text = models.TextField()
    pub_date = models.DateField()
    tags = models.ManyToManyField(Tag)
    startups = models.ManyToManyField(Startup)

    class Meta:
        get_latest_by = "pub_date"
        ordering = ["- pub_date", "title"]
        verbose_name = "blog post"

    def __str__(self):
        date_string = self.pub_date.strftime("%Y-%m-%d")
        return f"{self.title} on {date_string}"

