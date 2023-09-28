from django.urls import path
from .views import IndexView, UpdateView, get_permmissions

urlpatterns = [
    path("", IndexView.as_view(), name="managment_index"),
    path("update/<str:pk>", UpdateView.as_view(), name="managment_update"),
    path("get-permissions/<str:pk>/", get_permmissions, name="get_permmissions")
]
