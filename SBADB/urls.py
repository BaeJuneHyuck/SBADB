from django.urls import path, include
from rest_framework.routers import DefaultRouter

from SBADB.views import index, HeroViewSet, hero_edit, hero_new

urlpatterns = [
    path('', index),
    path('new/', hero_new),
    path('<int:pk>/edit/', hero_edit)
    # 정규 표현식이 포함된것
    # re_path(~~)잇음
]

router = DefaultRouter()
router.register('hero', HeroViewSet)

urlpatterns +=[
    path('api/v1/', include(router.urls))
]