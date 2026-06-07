from rest_framework.routers import DefaultRouter
from django.urls import path,include

from apps.users.views import UserViewSet

router = DefaultRouter()
router.register('',UserViewSet,basename='users')

urlpatterns = [
    path('',view=include(router.urls)),
]
