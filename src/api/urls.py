from django.urls import path
from .views import (
	getCharacterById,
)

urlpatterns = [
    path('character/<int:id>/', getCharacterById),
]
