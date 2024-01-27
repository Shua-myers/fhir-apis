from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path("Practitioner/", views.practitioner_list),
    path("Practitioner/<int:pk>/", views.practitioner_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
