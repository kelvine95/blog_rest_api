from django.db import models

from django_extensions.db.fields import AutoSlugField
class Tag(models.Model): 
    """Labels to help categorize data"""

    name = models.CharField(max_length=31, unique=True)
    slug = AutoSlugField(
        help_text="A label for URL config.",
        max_length=31,
        populate_from=["name"],
    )

    class Meta:
        ordering = ["name"]
    def __str__(self):
        return self.name

class Startup(models.Model):
    """"Data about a Startup company"""
    name = models.CharField(max_length = 32, db_index = True)
    slug = models.SlugField(max_length = 32, unique = True, help_text = "A label for URL config")
    description = models.TextField()
    founded_date = models.DateField("date founded")
    contact = models.EmailField()
    website = models.URLField(max_length = 255)
    tags = models.ManyToManyField(Tag)

    class Meta:
        get_latest_by = "founded_date"
        ordering = ["name"]

    def __str__(self):
        return self.name

class NewsLink(models.Model):
    """Link to external sources about Startup"""
    title = models.CharField(max_length = 32)
    slug = models.SlugField(max_length = 32, help_text = "A label for URL config")
    pub_date = models.DateField("date published")
    link  = models.URLField(max_length = 255)
    startup = models.ForeignKey(Startup, on_delete = models.CASCADE)

    class Meta:
        get_latest_by = "pub_date"
        ordering = ["-pub_date"]
        unique_together = ("slug", "startup")
        verbose_name = "news article"
    def __str__(self):
        return f"{self.startup}: {self.title}"