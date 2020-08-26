from django.urls import include, path
from rest_framework import routers
from .views import (
	RatingCreate,
	CharacterView,
)

urlpatterns = [
    path('character/<int:id>/', CharacterView.as_view()),
    path('character/<int:id>/rating/', RatingCreate.as_view()),
]
