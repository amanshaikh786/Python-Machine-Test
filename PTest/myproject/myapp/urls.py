from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ProjectViewSet, ProjectAssignmentViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'assignments', ProjectAssignmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
