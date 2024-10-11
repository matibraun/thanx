from django.db import migrations

def preload_credit_transactions(apps, schema_editor):
    Transaction = apps.get_model('transaction', 'Transaction')

    transactions = [
        {"user_id": 1, "points": 600, "type_id": 1},
        {"user_id": 1, "points": 400, "type_id": 1},
        {"user_id": 2, "points": 500, "type_id": 1},
        {"user_id": 2, "points": 500, "type_id": 1},
        {"user_id": 3, "points": 25, "type_id": 1},
        {"user_id": 3, "points": 50, "type_id": 1},
        {"user_id": 4, "points": 30, "type_id": 1},
        {"user_id": 4, "points": 20, "type_id": 1},
        {"user_id": 5, "points": 700, "type_id": 1},
        {"user_id": 5, "points": 300, "type_id": 1},
        {"user_id": 6, "points": 60, "type_id": 1},
        {"user_id": 6, "points": 20, "type_id": 1},
        {"user_id": 7, "points": 400, "type_id": 1},
        {"user_id": 7, "points": 600, "type_id": 1},
        {"user_id": 8, "points": 5, "type_id": 1},
        {"user_id": 8, "points": 5, "type_id": 1},
        {"user_id": 9, "points": 15, "type_id": 1},
        {"user_id": 9, "points": 10, "type_id": 1},
        {"user_id": 10, "points": 500, "type_id": 1},
        {"user_id": 10, "points": 500, "type_id": 1}
    ]

    for transaction in transactions:
        new_transaction = Transaction(
            user_id=transaction.get("user_id"),
            points=transaction.get("points"),
            type_id=transaction.get("type_id"),
            )
        new_transaction.save()

class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_preload_transaction_types'),
        ('user', '0002_preload_users'),
    ]

    operations = [
        migrations.RunPython(preload_credit_transactions),
    ]
