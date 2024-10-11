from django.http import JsonResponse
from django.views import View

class RewardListView(View):
    def get(self, request):
        # Example dictionary of rewards
        rewards = {
            "rewards": [
                {"id": 1, "name": "Free Coffee", "cost": 50},
                {"id": 2, "name": "Discount Voucher", "cost": 100},
                {"id": 3, "name": "Gift Card", "cost": 150},
            ]
        }
        return JsonResponse(rewards)