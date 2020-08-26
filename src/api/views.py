import requests
from django.db.models import Avg
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Character, Rating
from .serializers import RatingSerializer


def getCharacterById(request, id):
	character = Character()
	link = "https://swapi.dev/api/people/" + str(id) + "/"
	response = requests.get(link)
	response = response.json()
	character.name = response['name']
	character.height = response['height']
	character.mass = response['mass']

	urlPlanet = response['homeworld']
	responsePlanet = requests.get(urlPlanet)
	responsePlanet = responsePlanet.json()
	residents = 0
	for i in responsePlanet['residents']:
		residents = residents + 1

	# Devuelve el valor máximo, caso contrario, devuelve 0.
	character_max_rating = Rating.objects.filter(character_id=id).order_by('score').last()

	if character_max_rating:
		score = character_max_rating.score
	else:
		score = 0

	# Calcula el promedio del campo score para el character solicitado.
	character_average_rating = Rating.objects.filter(character_id=id).aggregate(Avg('score'))

	urlSpecie = response['species']
	if urlSpecie:
		urlSpecie = str(urlSpecie)
		urlID = urlSpecie.split('/')[5]
		responseSpecie = requests.get("https://swapi.dev/api/species/" + urlID + "/")
		responseSpecie = responseSpecie.json()
		specie = responseSpecie['name']
	else:
		specie = []

	response = JsonResponse(
		{
			'name': character.name,
			'height': character.height,
			'mass': character.mass,
			'hair_color': response['hair_color'],
			'skin_color': response['skin_color'],
			'eye_color': response['eye_color'],
			'birth_year': response['birth_year'],
			'gender': response['gender'],
			'homeworld': {
				'name': responsePlanet['name'],
				'population': responsePlanet['population'],
				'known_residents_count': residents,
			},
			'species_name': specie,
			'average_rating': character_average_rating['score__avg'],
			'max_rating': score,
		}
	)
	return response


class RatingViewSet(viewsets.ModelViewSet):
	queryset = Rating.objects.all()
	serializer_class = RatingSerializer
