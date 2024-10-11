from django.db import migrations

def preload_rewards(apps, schema_editor):
    Reward = apps.get_model('reward', 'Reward')

    rewards = [
        {
            "name": "Free Coffee",
            "description": "Enjoy a free coffee of your choice.",
            "points_required": 50,
            "available": True
        },
        {
            "name": "Movie Ticket",
            "description": "Get a ticket for any movie screening.",
            "points_required": 100,
            "available": True
        },
        {
            "name": "Discount Voucher",
            "description": "Receive a 20% discount on your next purchase.",
            "points_required": 75,
            "available": True
        },
        {
            "name": "Gift Card",
            "description": "A $10 gift card for your favorite store.",
            "points_required": 150,
            "available": True
        },
        {
            "name": "Dinner for Two",
            "description": "Enjoy a complimentary dinner for two at our restaurant.",
            "points_required": 300,
            "available": False
        },
        {
            "name": "Fitness Class Pass",
            "description": "One free pass for a fitness class of your choice.",
            "points_required": 100,
            "available": True
        },
        {
            "name": "Book of the Month",
            "description": "Receive a free book each month from our selection.",
            "points_required": 200,
            "available": True
        },
        {
            "name": "Personalized T-Shirt",
            "description": "Get a custom-designed T-shirt with your choice of text.",
            "points_required": 120,
            "available": True
        },
        {
            "name": "Spa Day",
            "description": "Enjoy a relaxing spa day with treatments included.",
            "points_required": 500,
            "available": False
        },
        {
            "name": "Travel Voucher",
            "description": "Receive a $50 voucher for your next travel booking.",
            "points_required": 400,
            "available": True
        }
    ]

    for reward in rewards:
        new_reward = Reward(
            name=reward.get("name"),
            description=reward.get("description"),
            points_required=reward.get("points_required"),
            available=reward.get("available"),
            )
        new_reward.save()

class Migration(migrations.Migration):

    dependencies = [
        ('reward', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(preload_rewards),
    ]
