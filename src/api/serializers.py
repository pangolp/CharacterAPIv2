from rest_framework import serializers
from .models import Planet, Character, Rating


class PlanetSerializer(serializers.ModelSerializer):

	class Meta:
		fields = (
			'name',
			'population',
			'known_residents_count'
		)
		model = Planet


class CharacterSerializer(serializers.ModelSerializer):

	class Meta:
		fields = (
			'name',
			'height',
			'mass',
			'hair_color',
			'skin_color',
			'eye_color',
			'birth_year',
			'gender',
			'homeworld',
			'species_name',
			'average_rating',
			'max_rating'
		)
		model = Character


class RatingSerializer(serializers.ModelSerializer):

	class Meta:
		fields = (
			'character_id',
			'score'
		)
		model = Rating
