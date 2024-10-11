from rest_framework import serializers

class RewardSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    points_required = serializers.IntegerField()
    available = serializers.BooleanField(default=True)

class RewardOutputSerializer(RewardSerializer):
    id = serializers.IntegerField(read_only=True)