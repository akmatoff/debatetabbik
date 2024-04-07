from django.urls import path
from .views import UserDetails, UsersList, UserData, google_auth_callback

app_name = "users"

urlpatterns = [
    path("", UsersList.as_view(), name="Users list"),
    path("<int:pk>", UserDetails.as_view(), name="User details"),
    path("get_userdata/", UserData.as_view(), name="User data"),
    path("google-auth-callback/", google_auth_callback, name="Google auth callback"),
]
