from rest_framework import serializers
from .models import Rating


class RatingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Rating
		fields = ['character_id', 'score']
