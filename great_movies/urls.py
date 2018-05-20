from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token

from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from movies import views

router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet)
router.register(r'persons', views.PersonViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^docs/', include_docs_urls(title='Movies Api')),
]
