from django.urls import include, path
from rest_framework import routers
from .views import (
	getCharacterById,
	RatingViewSet,
)

router = routers.DefaultRouter()
router.register('ratings', RatingViewSet)

urlpatterns = [
	path('', include(router.urls)),
    path('character/<int:id>/', getCharacterById),
]
