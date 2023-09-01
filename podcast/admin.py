from django.contrib import admin
from .models import Podcast, DashboardModel, Archive, ArchiveTags


admin.site.register(Podcast)
admin.site.register(DashboardModel)
admin.site.register(Archive)
admin.site.register(ArchiveTags)