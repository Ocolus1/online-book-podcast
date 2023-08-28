from django.shortcuts import render, get_object_or_404
from .models import Podcast, DashboardModel
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


def dashboard(request):
    dashboardList = DashboardModel.objects.all()
    
    content = {
        'dashboardList': dashboardList
    }
    return render(request, "podcast/dashboard.html", content)