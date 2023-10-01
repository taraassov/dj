from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from .apps import CatalogConfig
from .views import HomeView, GoodsView

app_name = CatalogConfig.name


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('goods/', GoodsView.as_view(), name='goods'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)