from django.shortcuts import render, get_object_or_404
from .models import Podcast, DashboardModel, Archive
import re
import requests
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound, VideoUnavailable
from datetime import datetime
import json
import tweepy



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


def reviews(request):
    
    return render(request, "podcast/review.html")


def archive_list(request):
    archives = Archive.objects.all().order_by("-id")
    
    content = {
        'archives': archives
    }
    return render(request, "podcast/archive/home.html", content)


def archive_detail(request, archive_slug):
    archive = Archive.objects.filter(slug=archive_slug).first()
    
    content = {
        'archive': archive
    }
    return render(request, "podcast/archive/archive_detail.html", content)