from rest_framework import serializers
from .models import Student, DocType
from rest_framework.decorators import detail_route


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('pk', 'name', 'lastname', 'doc_type', 'doc_number', 'email', 'url', 'created_on', 'updated_on')

    @detail_route(methods=['posts'])
    def subscribe_to_mailman(self):
        pass


class DocTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DocType
        fields = ('doc_type', )
