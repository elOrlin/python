"""
URL mapping for the user api.
"""
from django.urls import path
from user.views import (
    CreateUserView,
    CreateTokenView,
    ManagerUserView
)

app_name = 'User'

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('token/', CreateTokenView.as_view(), name='token'),
    path('me/', ManagerUserView.as_view(), name='me')
]
