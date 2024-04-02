from django.urls import path
from .views import UserDetails, UsersList, UserData, google_auth_callback

urlpatterns = [
    path("users/", UsersList.as_view(), name="Users list"),
    path("users/<int:pk>", UserDetails.as_view(), name="User details"),
    path("get_userdata/", UserData.as_view(), name="User data"),
    path("google-auth-callback/", google_auth_callback, name="Google auth callback"),
]
