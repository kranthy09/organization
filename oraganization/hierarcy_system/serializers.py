from rest_framework import serializers
from django.contrib.auth.models import User, Group
from hierarcy_system.models import OrganizationUser, Portfolio


class OrgUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationUser
        fields = "__all__"


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"
