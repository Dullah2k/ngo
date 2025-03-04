from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include('landing_page.urls', namespace='landing_page')),
  path('user_auth/', include('user_auth.urls', namespace='user_auth')),
  path('organization/', include('organization.urls', namespace='organization')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)