from django.core.exceptions import ValidationError


def score_validation(value):
	if value > 5 or value < 1:
		raise ValidationError('El valor del score debe ser un número entre 1 y 5.')
