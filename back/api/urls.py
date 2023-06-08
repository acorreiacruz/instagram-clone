from django.urls import path

from . import views

app_name = "api"

urlpatterns = [
    path("records/", views.RecordAPIView.as_view(), name="record-api-list"),
    path("records/<int:id>/", views.RecordAPIView.as_view(), name="record-api-detail"),
]
