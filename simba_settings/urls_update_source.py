class UrlsUpdateSource:
    def __init__(self):
        self.urls_import = [
"""
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
"""
        ]
        self.urls_patterns = [
"""
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
"""
        ]
