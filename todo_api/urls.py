from django.urls import path, include
from todo_api import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'todos', views.TodoViewSet, basename='todos')

urlpatterns = [
    path('', include(router.urls))
]


# urlpatterns = format_suffix_patterns(urlpatterns)