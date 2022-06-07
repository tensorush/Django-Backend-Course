from django.contrib import admin
from django.urls import path, re_path, include

from rest_framework.routers import DefaultRouter

from web.views import get_home, get_index
from api.views import SystemViewSet, CategoryViewSet


router = DefaultRouter()

router.register('api/system', SystemViewSet, basename='systems')
router.register('api/category', CategoryViewSet, basename='categories')

urlpatterns = [
    path('', get_home, name='home'),
    path('admin/', admin.site.urls),
    path('backend/', get_home, name='backend'),
    re_path('web/(?P<user_name>\w+)/', get_index),
]

urlpatterns += router.urls
