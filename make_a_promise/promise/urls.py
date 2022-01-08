from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Promise_Api

router = DefaultRouter()
router.register(r"promise-api", Promise_Api, basename="promise_Api")


urlpatterns = [
path('', include(router.urls))
]


