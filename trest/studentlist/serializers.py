from rest_framework import serializers
from .models import Student, DocType


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('pk', 'name', 'lastname', 'doc_type', 'doc_number', 'email', 'url', 'created_on', 'updated_on')



class DocTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DocType
        fields = ('doc_type', )
