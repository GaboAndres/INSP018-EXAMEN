from django.conf.urls import url, patterns
from pauta.view import InicioView


urlpatterns = [
    url(r'^', InicioView.as_view(), name=inicio),
    ,
]
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)