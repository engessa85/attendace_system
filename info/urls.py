from django.urls import path
from .views import IndexView, MainInfoView, DialyReportView

urlpatterns = [
    path("", MainInfoView.as_view(), name="MainInfoView"),
    path("month-info", IndexView.as_view(), name="month-info"),
    path("day-info", DialyReportView.as_view(), name="day-info"),

]
