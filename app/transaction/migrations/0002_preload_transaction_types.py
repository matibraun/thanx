from django.db import migrations

def preload_transaction_types(apps, schema_editor):
    TransactionType = apps.get_model('transaction', 'TransactionType')

    transaction_types_statuses = ['credit', 'debit']

    for transaction_type in transaction_types_statuses:
        new_transaction_type = TransactionType(name=transaction_type)
        new_transaction_type.save()



class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(preload_transaction_types),
    ]
