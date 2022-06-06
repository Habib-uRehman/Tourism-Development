from xml.etree.ElementInclude import include
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    # path('jet/', include('jet.urls', 'jet')),
    # path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('', include('pages.urls')),
    path('', include('restraunt.urls')),
    path('', include('hotel.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('tourist.urls')),
    path('', include('travel.urls')),
    path('admin/', admin.site.urls)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
