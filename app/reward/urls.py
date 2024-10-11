from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AvailableRewardViewSet, RedemptionViewSet, RewardViewSet

router = DefaultRouter()
router.register(r'rewards', RewardViewSet, basename='reward')
router.register(r'redemptions', RedemptionViewSet, basename='redemption')

urlpatterns = [
    path('', include(router.urls)),
    path('available-rewards/', AvailableRewardViewSet.as_view({'get': 'list'}), name='available-rewards'),
    path('redemptions/user/<int:user_id>/', RedemptionViewSet.as_view({'get': 'retrieve'}), name='user-redemptions'),
]