from django.urls import path,include
from first_app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('upload/', views.upload_pdf, name='upload'),
    path('download/<int:pk>/', views.download_converted, name='download'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
