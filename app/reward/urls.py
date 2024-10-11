from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AvailableRewardViewSet, RewardViewSet

router = DefaultRouter()
router.register(r'rewards', RewardViewSet, basename='reward')

urlpatterns = [
    path('', include(router.urls)),
    path('available-rewards/', AvailableRewardViewSet.as_view({'get': 'list'}), name='available-rewards'),
]