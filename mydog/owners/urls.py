from django.urls import path
from .views import OwnersView

urlpatterns = [
    path("", OwnersView.as_view())
]