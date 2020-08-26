import requests
from django.http import JsonResponse
from .models import Character


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
			'species_name': '',
			'average_rating': 4.5,
			'max_rating': 5,
		}
	)
	return response
