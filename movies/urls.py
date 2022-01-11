from django.contrib import admin
from django.urls import path
from movies.views import *

urlpatterns = [
	path('movies', movies_api,name='all_movies')
]