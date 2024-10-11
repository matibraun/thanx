from rest_framework import serializers

class RewardSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    points_required = serializers.IntegerField()
    available = serializers.BooleanField(default=True)

class RewardOutputSerializer(RewardSerializer):
    id = serializers.IntegerField(read_only=True)

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)

class RedemptionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    reward = RewardSerializer()
    user = UserSerializer()
    created_at = serializers.DateTimeField()