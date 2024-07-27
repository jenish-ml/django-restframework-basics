from rest_framework import serializers
from .models import User, Team

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    team_info = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'
        depth = 1

    def get_team_info(self, obj):
        return "obj.team.name"
    
