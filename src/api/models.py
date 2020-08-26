from django.db import models


class Planet(models.Model):
	name = models.CharField(max_length=50, help_text='ex. Tatooine')
	population = models.CharField(max_length=50, help_text='ex. 200000')
	known_residents_count = models.SmallIntegerField('known residents count', help_text='ex. 9')

	def __str__(self):
		return self.name

	class Meta:
		abstract = True


class Character(models.Model):
	name = models.CharField(max_length=50, help_text='ex. Luke Skywalker')
	height = models.CharField(max_length=3, help_text='ex. 172')
	mass = models.CharField(max_length=2, help_text='ex. 77')
	hair_color = models.CharField('hair color', max_length=25, help_text='ex. blond')
	skin_color = models.CharField('skin color', max_length=25, help_text='ex. fair')
	eye_color = models.CharField('eye color', max_length=50, help_text='ex. blue')
	birth_year = models.CharField('birth year', max_length=5, help_text='ex. 19BBY')
	gender = models.CharField(max_length=10, help_text='ex. male')
	homeworld = models.ForeignKey(Planet, on_delete=models.CASCADE)
	species_name = models.CharField('species name', max_length=50, help_text='ex. Human')
	average_rating = models.FloatField('average rating', help_text='ex. 3.5')
	max_rating = models.SmallIntegerField('max rating', help_text='ex. 5')

	def __str__(self):
		return self.name

	class Meta:
		abstract = True
