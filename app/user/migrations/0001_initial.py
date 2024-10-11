# Generated by Django 5.1.2 on 2024-10-11 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('country_code', models.CharField(blank=True, max_length=5, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('document_type', models.CharField(max_length=30)),
                ('document_number', models.CharField(max_length=50)),
                ('address', models.TextField(blank=True, null=True)),
                ('nationality', models.CharField(blank=True, max_length=50, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('civil_state', models.CharField(blank=True, max_length=15, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
