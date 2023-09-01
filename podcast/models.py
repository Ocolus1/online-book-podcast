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
    
class DashboardModel(models.Model):
    name = models.CharField(max_length=200)
    mission = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='dashboard/logo/', blank=True, null=True)
    website_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    discord_url = models.URLField(blank=True, null=True)
    join_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"
    

class ArchiveTags(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Archive(models.Model):
    slug = AutoSlugField(populate_from='title', unique=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='archive/profile/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='archive/thumbnail/', blank=True, null=True)
    content = RichTextField()
    tags = models.ManyToManyField(ArchiveTags, related_name="archives", blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.slug}"