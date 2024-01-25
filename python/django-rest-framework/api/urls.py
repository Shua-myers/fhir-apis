from django.urls import path
from api import views

urlpatterns = [
    path("practitioners/", views.practitioner_list),
    path("practitioners/<int:pk>/", views.practitioner_detail),
]
