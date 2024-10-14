import argparse
from api_client import APIClient

# Initialize the API client
client = APIClient()

def list_users(args):
    users = client.get_users()
    for user in users:
        print(f"""
        ID: {user['id']}
        Email: {user['email']}
        First Name: {user['first_name']}
        Last Name: {user['last_name']}
        Country Code: {user['country_code'] or 'N/A'}
        Phone: {user['phone'] or 'N/A'}
        Document Type: {user['document_type']}
        Document Number: {user['document_number']}
        Address: {user['address'] or 'N/A'}
        Nationality: {user['nationality'] or 'N/A'}
        Gender: {user['gender'] or 'N/A'}
        Civil State: {user['civil_state'] or 'N/A'}
        Created At: {user['created_at']}
        Updated At: {user['updated_at']}
        """)

def create_user(args):

    user_data = {
        'email': args.email,
        'first_name': args.first_name,
        'last_name': args.last_name,
        'country_code': args.country_code,
        'phone': args.phone,
        'document_type': args.document_type,
        'document_number': args.document_number,
        'address': args.address,
        'nationality': args.nationality,
        'gender': args.gender,
        'civil_state': args.civil_state,
    }
    
    response = client.create_user(user_data)
    
    if response.status_code == 201:
        print(f"User created successfully: {response.json()}")
    else:
        print(f"Failed to create user. Status code: {response.status_code}")

def get_user_points_balance(args):
    points_balance = client.get_user_points_balance(args.user_id)

    if 'points_balance' in points_balance:
        print(f"User ID: {args.user_id} has {points_balance['points_balance']} points.")
    else:
        print(f"Failed to retrieve points balance for User ID: {args.user_id}.")

def list_rewards(args):
    rewards = client.get_rewards()
    for reward in rewards:
        print(f"ID: {reward['id']}, Name: {reward['name']}, Points Required: {reward['points_required']}, Available: {reward['available']}")

def list_available_rewards(args):
    available_rewards = client.get_available_rewards()
    for reward in available_rewards:
        print(f"ID: {reward['id']}, Name: {reward['name']}, Points Required: {reward['points_required']}")

def create_reward(args):
    reward_data = {
        "name": args.name,
        "points_required": args.points_required,
        "description": args.description
    }

    response = client.create_reward(reward_data)
    
    if response.status_code == 201:
        print(f"Reward created successfully: {response.json()}")
    else:
        print(f"Failed to create reward. Status code: {response.status_code}")

def list_redemptions(args):
    redemptions = client.get_redemptions()
    
    if redemptions:
        for redemption in redemptions:
            print(f"""
            ID: {redemption['id']}
            User: {redemption['user']['email']}
            Reward: {redemption['reward']['name']}
            Created At: {redemption['created_at']}
            """)
    else:
        print("No redemptions found.")


def list_redemptions_by_user(args):
    user_id = args.user_id
    redemptions = client.get_redemptions_by_user(user_id)
    
    if isinstance(redemptions, dict) and 'detail' in redemptions:
        print(f"No redemptions found for user with ID: {user_id}.")

    elif redemptions:
        for redemption in redemptions:
            print(f"""
            ID: {redemption['id']}
            User: {redemption['user']['email']}
            Reward: {redemption['reward']['name']}
            Created At: {redemption['created_at']}
            """)

    else:
        print(f"Failed to retrieve redemptions for user with ID: {user_id}.")

def redeem_reward(args):
    user_id = args.user_id
    reward_id = args.reward_id

    # Call the client function to redeem the reward
    response = client.redeem_reward(user_id, reward_id)

    if response.status_code == 201:
        print(f"Reward redeemed successfully: {response.json()}")
    else:
        print(f"Failed to redeem reward. Status code: {response.status_code}")
        print(response.json())

def list_transactions(args):
    transactions = client.get_all_transactions()

    if transactions:
        for transaction in transactions:
            print(f"""
            ID: {transaction['id']}
            User: {transaction['user']['email']}
            Points: {transaction['points']}
            Type: {transaction['type']['name']}
            Created At: {transaction['created_at']}
            """)
    else:
        print("No transactions found.")



# Set up command-line arguments
def main():
    parser = argparse.ArgumentParser(description="CLI for interacting with the backend rewards system.")
    
    subparsers = parser.add_subparsers()

    # List all users command
    list_users_parser = subparsers.add_parser('list-users', help='List all users')
    list_users_parser.set_defaults(func=list_users)

    # Command for creating a new user
    parser_create_user = subparsers.add_parser('create-user', help='Create a new user')
    parser_create_user.add_argument('email', type=str, help='User email')
    parser_create_user.add_argument('first_name', type=str, help='First name')
    parser_create_user.add_argument('last_name', type=str, help='Last name')
    parser_create_user.add_argument('--country_code', type=str, help='Country code', default='')
    parser_create_user.add_argument('--phone', type=str, help='Phone number', default='')
    parser_create_user.add_argument('--document_type', type=str, help='Document type')
    parser_create_user.add_argument('--document_number', type=str, help='Document number')
    parser_create_user.add_argument('--address', type=str, help='Address', default='')
    parser_create_user.add_argument('--nationality', type=str, help='Nationality', default='')
    parser_create_user.add_argument('--gender', type=str, help='Gender', default='')
    parser_create_user.add_argument('--civil_state', type=str, help='Civil state', default='')
    parser_create_user.set_defaults(func=create_user)    

    parser_points_balance = subparsers.add_parser('get-user-points-balance', help="Get a user's points balance")
    parser_points_balance.add_argument('user_id', type=int, help='User ID to retrieve points balance for')
    parser_points_balance.set_defaults(func=get_user_points_balance)

    list_rewards_parser = subparsers.add_parser('list-rewards', help='List all rewards')
    list_rewards_parser.set_defaults(func=list_rewards)

    list_available_rewards_parser = subparsers.add_parser('list-available-rewards', help='List available rewards')
    list_available_rewards_parser.set_defaults(func=list_available_rewards)

    parser_create_reward = subparsers.add_parser('create-reward', help='Create a new reward')
    parser_create_reward.add_argument('name', type=str, help='Name of the reward')
    parser_create_reward.add_argument('points_required', type=int, help='Points required for the reward')
    parser_create_reward.add_argument('--description', type=str, help='Description of the reward', default=None)
    parser_create_reward.set_defaults(func=create_reward)

    parser_list_redemptions = subparsers.add_parser('list-redemptions', help='List all redemptions')
    parser_list_redemptions.set_defaults(func=list_redemptions)

    parser_list_redemptions_by_user = subparsers.add_parser('list-redemptions-by-user', help='List redemptions by user')
    parser_list_redemptions_by_user.add_argument('user_id', type=int, help='User ID to list redemptions for')
    parser_list_redemptions_by_user.set_defaults(func=list_redemptions_by_user)

    redeem_parser = subparsers.add_parser('redeem-reward', help="Redeem a reward for a user")
    redeem_parser.add_argument('--user-id', type=int, required=True, help="ID of the user")
    redeem_parser.add_argument('--reward-id', type=int, required=True, help="ID of the reward")
    redeem_parser.set_defaults(func=redeem_reward)

    transactions_parser = subparsers.add_parser('list-transactions', help="List all transactions")
    transactions_parser.set_defaults(func=list_transactions)

    # Parse and execute the appropriate function based on the arguments provided
    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()