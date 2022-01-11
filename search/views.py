from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
	FilteringFilterBackend,
    CompoundSearchFilterBackend,
)
from .documents import * 
from .serializers import *

# Create your views here.

class MoviesDocumentView(DocumentViewSet):
	document = NewsDocument
	serializer_class = NewsDocumentSerializer

	filter_backends = [
		FilteringFilterBackend,
		CompoundSearchFilterBackend,
	]


	search_fields = ('locations', 'fun_facts')
	multi_match_search_fields = ('locations', 'fun_facts')
	match_phrase_prefix = ('locations', 'fun_facts')
	filter_fields = {
		'locations' : 'locations',
		'fun_facts' : 'fun_facts'
	}