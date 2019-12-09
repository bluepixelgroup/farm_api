from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers
from farm.views import PersonViewSet, FarmerViewSet

router = routers.DefaultRouter()
router.register(r'persons', PersonViewSet)
router.register(r'farmers', FarmerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'api/', include(router.urls))
]
