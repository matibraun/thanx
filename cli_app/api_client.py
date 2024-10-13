import requests

class APIClient:
    BASE_URL = 'http://127.0.0.1:8000/'

    def get_users(self):
        response = requests.get(f'{self.BASE_URL}user/users/')
        return response.json()

    def create_user(self, user_data):
        response = requests.post(f'{self.BASE_URL}user/users/', json=user_data)
        return response

    def get_user_points_balance(self, user_id):
        response = requests.get(f'{self.BASE_URL}user/users/{user_id}/points-balance/')
        return response.json()
    
    def get_rewards(self):
        response = requests.get(f'{self.BASE_URL}reward/rewards/')
        return response.json()
    
    def create_reward(self, reward_data):
        response = requests.post(f'{self.BASE_URL}reward/rewards/', json=reward_data)
        return response

    def get_available_rewards(self):
        response = requests.get(f'{self.BASE_URL}reward/available-rewards/')
        return response.json()
    
    def get_redemptions(self):
        response = requests.get(f'{self.BASE_URL}reward/redemptions/')
        return response.json()
    
    def get_redemptions_by_user(self, user_id):
        response = requests.get(f'{self.BASE_URL}reward/redemptions/user/{user_id}/')
        return response.json()

    def redeem_reward(self, user_id, reward_id):
        response = requests.post(f'{self.BASE_URL}reward/redemptions/', json={
            'user_id': user_id,
            'reward_id': reward_id
        })
        return response
    
    def get_all_transactions(self):
        response = requests.get(f'{self.BASE_URL}transaction/transactions/')
        return response.json()