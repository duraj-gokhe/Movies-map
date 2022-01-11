from django.contrib import admin
from movies.models import Movies

# Register your models here.
class MoviesAdmin(admin.ModelAdmin):
	list_display = ('title', 'release_year', 'locations', 'fun_facts', 'production_company', 'director', 'writer', 'actor_1', 'actor_2', 'actor_3')

admin.site.register(Movies, MoviesAdmin)


