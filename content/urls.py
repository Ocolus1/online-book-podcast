from django.urls import path
from .views import home, section_detail
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/book/1', permanent=True)),
    path('book/<int:id>', home, name="book_home"),
    path('book/<int:id>/<slug:chapter_slug>/', section_detail, name='section_detail'),
]
