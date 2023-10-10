from users.models import CustomUser
from rest_framework import serializers

class CustomUserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ["email", "password", "username"]