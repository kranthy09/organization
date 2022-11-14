from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import generics
from hierarcy_system.serializers import OrgUserSerializer, PortfolioSerializer, UserSerializer, GroupSerializer
from hierarcy_system.models import OrganizationUser, Portfolio


# Create your views here.
class OrgUserCreateRetrieveViewSet(mixins.CreateModelMixin,
                                    mixins.ListModelMixin,
                                    mixins.RetrieveModelMixin,
                                    viewsets.GenericViewSet):
    queryset = OrganizationUser.objects.all()
    serializer_class = OrgUserSerializer


class OrgUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrganizationUser.objects.all()
    serializer_class = OrgUserSerializer

class PortfolioCreateRetrieveViewSet(mixins.CreateModelMixin,
                                    mixins.ListModelMixin,
                                    mixins.RetrieveModelMixin,
                                    viewsets.GenericViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class PortfolioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
