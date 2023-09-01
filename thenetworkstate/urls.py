from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from podcast.views import dashboard, archive_list, archive_detail, reviews

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('', include('content.urls')),
    path('dashboard', dashboard, name="dashboard"),
    path('reviews', reviews, name="reviews"),
    path('archive', archive_list, name="archive_list"),
    path('archive/<slug:archive_slug>/', archive_detail, name="archive_detail"),
    path('podcast/', include('podcast.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)