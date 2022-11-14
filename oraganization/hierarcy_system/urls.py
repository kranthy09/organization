from django.contrib import admin
from django.urls import path, include
from hierarcy_system.views import (OrgUserCreateRetrieveViewSet,
                                    OrgUserDetail,
                                    PortfolioCreateRetrieveViewSet,
                                    PortfolioDetail,
                                    UserList,
                                    UserDetail,
                                    GroupList,
                                    GroupDetail)

urlpatterns = [
    path('orgusers/', OrgUserCreateRetrieveViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('orgusers/<int:pk>/', OrgUserDetail.as_view()),
    path('portfolios/', PortfolioCreateRetrieveViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('portfolios/<int:pk>/', PortfolioDetail.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('groups/', GroupList.as_view()),
    path('groups/<int:pk>/', GroupDetail.as_view()),
]
