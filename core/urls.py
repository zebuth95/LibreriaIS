from django.urls import path
from .views import SignUpView, detalleslug

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('libro/<slug:slug>/', detalleslug, name='libro'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

