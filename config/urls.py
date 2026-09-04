from django.contrib import admin
from django.urls import path, include

from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
                  # Panel URLs - include each panel you installed
                  path('admin/dj-redis-panel/', include('dj_redis_panel.urls')),
                  path('admin/dj-cache-panel/', include('dj_cache_panel.urls')),
                  path('admin/dj-urls-panel/', include('dj_urls_panel.urls')),
                  path('admin/dj-celery-panel/', include('dj_celery_panel.urls')),
                  path('admin/dj-signals-panel/', include('dj_signals_panel.urls')),
                  # Control Room dashboard
                  path('admin/dj-control-room/', include('dj_control_room.urls')),
                  path('admin/', admin.site.urls),
              ] + debug_toolbar_urls()
