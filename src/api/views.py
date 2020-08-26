import requests
from django.db.models import Avg
from rest_framework import status
from .models import Planet, Character, Rating
from .serializers import PlanetSerializer, CharacterSerializer, RatingSerializer
from rest_framework.generics import CreateAPIView

from rest_framework.response import Response
from rest_framework.views import APIView


class CharacterView(APIView):

	def get(self, request, id):

		character = Character()
		planet = Planet()

		if id <= 83:
			link = "https://swapi.dev/api/people/" + str(id) + "/"
			response = requests.get(link)
			response = response.json()

			character.name = response['name']
			character.height = response['height']
			character.mass = response['mass']
			character.hair_color = response['hair_color']
			character.skin_color = response['skin_color']
			character.eye_color = response['eye_color']
			character.birth_year = response['birth_year']
			character.gender = response['gender']

			urlPlanet = response['homeworld']
			responsePlanet = requests.get(urlPlanet)
			responsePlanet = responsePlanet.json()

			residents = 0
			for i in responsePlanet['residents']:
				residents = residents + 1

			planet.name = responsePlanet['name']
			planet.population = responsePlanet['population']
			planet.known_residents_count = residents

			character.homeworld = planet

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
				specie = ''

			character.species_name = specie
			character.average_rating = character_average_rating['score__avg']
			character.max_rating = score

			serializer = CharacterSerializer(character)
			return Response(serializer.data)
		else:
			return Response('El valor del id, no se puede superar el 83.')


class RatingCreate(CreateAPIView):

	serializer_class = RatingSerializer

	def post(self, request, id):
		serializer = RatingSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(character_id=id)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
