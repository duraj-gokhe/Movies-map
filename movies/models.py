from django.db import models

# Create your models here.
class Movies(models.Model):
	title = models.CharField(max_length=255)
	release_year = models.CharField(max_length=100)
	locations = models.CharField(max_length=500, null = True)
	fun_facts = models.CharField(max_length=500, null = True)
	production_company = models.CharField(max_length=300)
	director = models.CharField(max_length=150)
	writer = models.CharField(max_length=150)
	actor_1 = models.CharField(max_length=150, null = True)
	actor_2 = models.CharField(max_length=150, null = True)
	actor_3 = models.CharField(max_length=150, null = True)

	def __str__(self):
		return '%s' % self.title

