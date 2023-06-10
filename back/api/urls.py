from api import views
from django.urls import path

app_name = "api"

urlpatterns = [
    path("records/", views.RecordAPIView.as_view(), name="record-api-list"),
    path("records/<int:id>/", views.RecordAPIView.as_view(), name="record-api-detail"),
    path("images/", views.ImageAPIView.as_view(), name="image-api-list"),
    path("images/<int:id>/", views.ImageAPIView.as_view(), name="image-api-detail")
]
