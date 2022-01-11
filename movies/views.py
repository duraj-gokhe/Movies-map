from django.http import JsonResponse
from movies.models import Movies
import requests, json

# Call external api to get movies data and send in my own api for security purpose	
def movies_api(request):
	url = 'https://data.sfgov.org/resource/yitu-d5am.json'
	all_data = requests.get(url)
	response = all_data.json()
	for data in response:
		Movies.objects.create(
			title = data.get('title'),
			release_year = data.get('release_year'),
			locations = data.get('locations'),
			fun_facts = data.get('fun_facts'),
			production_company = data.get('production_company'),
			director = data.get('director'),
			writer = data.get('writer'),
			actor_1 = data.get('actor_1'),
			actor_2 = data.get('actor_2'),
			actor_3 = data.get('actor_3')
		)
	context = {"Message":"User details successfully Updated"}
	return JsonResponse(context, content_type= 'application/json')