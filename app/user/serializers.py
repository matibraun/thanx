from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(max_length=50, required=True)
    last_name = serializers.CharField(max_length=50, required=True)
    country_code = serializers.CharField(max_length=5, required=False)
    phone = serializers.CharField(max_length=15, required=False)
    document_type = serializers.CharField(max_length=30, required=True)
    document_number = serializers.CharField(max_length=50, required=True)
    address = serializers.CharField(required=False, allow_blank=True)
    nationality = serializers.CharField(max_length=50, required=False, allow_blank=True)
    gender = serializers.CharField(max_length=50, required=False, allow_blank=True)
    civil_state = serializers.CharField(max_length=50, required=False, allow_blank=True)

class UserOutputSerializer(UserSerializer):
    id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)