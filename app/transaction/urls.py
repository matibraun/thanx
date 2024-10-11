from django.urls import path
from .views import RewardListView

urlpatterns = [
    path('', RewardListView.as_view(), name='reward-list'),
]