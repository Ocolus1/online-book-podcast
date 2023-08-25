from django.db import models
from ckeditor.fields import RichTextField
from django_extensions.db.fields import AutoSlugField
from django.core.validators import FileExtensionValidator

# Create your models here.
class Book(models.Model):
    book_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    amazon_url = models.TextField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='books/covers/', blank=True, null=True)
    pdf_file = models.FileField(upload_to='books/pdfs/', blank=True, null=True, validators=[FileExtensionValidator(['pdf'])])

    def __str__(self):
        return self.title

class BookChapter(models.Model):
    book = models.ForeignKey(Book, related_name='chapters', on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='title', unique=True)
    title = models.CharField(max_length=200)
    content = RichTextField()
    sequence_number = models.FloatField(null=True, blank=True,)  # The uniqueness now would be combination of book and sequence_number
    next_chapter = models.OneToOneField('self', null=True, blank=True, on_delete=models.SET_NULL)
    category_text = models.CharField(max_length=200, null=True, blank=True)
    category_id = models.IntegerField(null=True, blank=True)

    class Meta:
        unique_together = ['book', 'sequence_number']

    def __str__(self):
        return f"{self.book.title} - {self.title} - {self.slug} - {self.sequence_number}"

class Podcast(models.Model):
    title = models.CharField(max_length=200)
    video_url = models.URLField()
    transcript = models.TextField()
    youtube_url = models.URLField(blank=True, null=True)
    apple_url = models.URLField(blank=True, null=True)
    spotify_url = models.URLField(blank=True, null=True)