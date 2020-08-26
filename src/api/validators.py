from django.core.exceptions import ValidationError


def score_validation(value):
	if value > 5 or value < 1:
		raise ValidationError('El valor del score debe ser un número entre 1 y 5.')


def character_id_validation(value):
	if value <= 0 or value > 83:
		raise ValidationError('El character id, debe ser un número mayor que 0 y menor que 84.')
