from django_elasticsearch_dsl import Document, fields, Index
from movies.models import Movies

PUBLISHER_INDEX = Index('elastic_movies')

PUBLISHER_INDEX.settings(
	number_of_shards = 1
	# number_of_replicas = 1
	)

@PUBLISHER_INDEX.doc_type
class NewsDocument(Document):
	id = fields.IntegerField(attr='id')
	title = fields.TextField(
		fields = {
			"raw" : {
				"type" : "keyword"
			}
		}
	)

	release_year = fields.TextField(
		fields = {
			"raw" : {
				"type" : "keyword"
			}
		}
	)

	locations = fields.TextField(
		fields = {
			"raw" : {
				"type" : "keyword"
			}
		}
	)

	fun_facts = fields.TextField(
		fields = {
			"raw" : {
				"type" : "keyword"
			}
		}
	)

	production_company = fields.TextField(
		fields = {
			"raw" : {
				"type" : "keyword"
			}
		}
	)

	director = fields.TextField(
		fields = {
			"raw" : {
				"type" : "keyword"
			}
		}
	)

	writer = fields.TextField(
		fields = {
			"raw" : {
				"type" : "keyword"
			}
		}
	)

	actor_1 = fields.TextField(
		fields = {
			"raw" : {
				"type" : "keyword"
			}
		}
	)

	actor_2 = fields.TextField(
		fields = {
			"raw" : {
				"type" : "keyword"
			}
		}
	)

	actor_3 = fields.TextField(
		fields = {
			"raw" : {
				"type" : "keyword"
			}
		}
	)

	class Django(object):
		model = Movies