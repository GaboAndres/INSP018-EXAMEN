

from django.conf.urls import url, patterns


urlpatterns = [
    url(r'^', ),
  
]
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)