from django.urls import path
from .views import home, podcast_detail

urlpatterns = [
    path('', home, name="podcast_home"),
    path('episode/<slug:podcast_slug>/', podcast_detail, name='podcast_detail'),
]
