from django.urls import path,include
from rest_framework import routers

from .views import index,FileViewSet

router = routers.DefaultRouter()
urlpatterns = [

    path('',index,name='index')

]
router.register('api',FileViewSet,'api')


urlpatterns += router.urls