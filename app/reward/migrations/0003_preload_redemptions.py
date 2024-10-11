from django.db import migrations

def preload_redemptions(apps, schema_editor):
    Redemption = apps.get_model('reward', 'Redemption')
    Reward = apps.get_model('reward', 'Reward')
    Transaction = apps.get_model('transaction', 'Transaction')

    redemptions = [
        {"user_id": 1, "reward_id": 3},
        {"user_id": 2, "reward_id": 2},
        {"user_id": 5, "reward_id": 1},
        {"user_id": 10, "reward_id": 9},
    ]

    for redemption in redemptions:
        reward_id = redemption.get("reward_id")
        user_id = redemption.get("user_id")

        new_redemption = Redemption(
            reward_id=reward_id,
            user_id=user_id,
        )
        new_redemption.save()

        reward = Reward.objects.get(id=reward_id)
        points_required = reward.points_required

        new_transaction = Transaction(
            user_id=user_id,
            points=-points_required,
            type_id=2
        )
        new_transaction.save()

class Migration(migrations.Migration):

    dependencies = [
        ('reward', '0002_preload_rewards'),
        ('user', '0002_preload_users'),
        ('transaction', '0003_preload_credit_transactions'),
    ]

    operations = [
        migrations.RunPython(preload_redemptions),
    ]