from django.db import models
from ckeditor.fields import RichTextField
from django_extensions.db.fields import AutoSlugField
from django.core.validators import FileExtensionValidator

# Create your models here.
class Podcast(models.Model):
    slug = AutoSlugField(populate_from='title', unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    thumbnail_image = models.ImageField(upload_to='podcast/thumbnail/', blank=True, null=True)
    transcript = RichTextField(blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)
    video_id = models.CharField(max_length=20, null=True, blank=True)
    apple_url = models.URLField(blank=True, null=True)
    spotify_url = models.URLField(blank=True, null=True)
    sequence_number = models.IntegerField(null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['sequence_number']

    def __str__(self):
        return f"{self.title} - {self.slug} - {self.sequence_number}"