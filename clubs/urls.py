from django.urls import path
from .views import get_clubs

urlpatterns = [
    path('clubs/', get_clubs, name="Clubs list")
]