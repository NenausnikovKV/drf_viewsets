from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


router = SimpleRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = router.urls
urlpatterns.append(path('', views.ApiRootView.as_view()))
urlpatterns = format_suffix_patterns(urlpatterns)