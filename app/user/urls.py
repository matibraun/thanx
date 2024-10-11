from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, UserPointsBalanceView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('users/<int:user_id>/points-balance/', UserPointsBalanceView.as_view(), name='user-points-balance'),
]