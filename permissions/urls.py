from django.urls import path
from .views import IndexView, UpdateView

urlpatterns = [
     path("", IndexView.as_view(), name="permissions_index"),
     path("permissions/<str:pk>", UpdateView.as_view(), name="permissions_update"),
]
