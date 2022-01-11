from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from movies.models import Movies
from .documents import *

class NewsDocumentSerializer(DocumentSerializer):
    class Meta:
        model = Movies
        document = NewsDocument
        fields = '__all__'

        def get_location(self, obj):
            try:
                obj.location.to_dict()
            except:
                return {}