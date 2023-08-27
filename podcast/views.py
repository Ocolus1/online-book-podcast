from django.shortcuts import render, get_object_or_404
from .models import Podcast
import re
import requests
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound, VideoUnavailable
from datetime import datetime
import json


def home(request):
    podcast = Podcast.objects.all().order_by('-sequence_number')
   
    content = {
        'podcasts': podcast
    }
    return render(request, "podcast/home.html", content)


def podcast_detail(request, podcast_slug):
    podcast = Podcast.objects.filter(slug=podcast_slug).first()
    
    content = {
        'podcast': podcast
    }
    return render(request, "podcast/podcast_detail.html", content)