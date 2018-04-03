import requests
from django.shortcuts import render, get_object_or_404
from .models import Student, DocType
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from .serializers import StudentSerializer, DocTypeSerializer


def index(request):
    latest_students = Student.objects.order_by('-created_on')[:5]
    context = {
        'latest_students': latest_students,
    }
    return render(request, 'studentlist/index.html', context)


def details(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    context = {
        'student': student
    }
    return render(request, 'studentlist/details.html', context)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @detail_route(methods=['post'])
    def subscribe_to_mailman(self, request, pk=None):
        print('extra function')
        student = self.get_object()
        data = {
            'email': student.email,
            'fullname': '{} {}'.format(student.name, student.lastname),
            'pw': student.doc_number,
            'pw-conf': student.doc_number,
            'digest': 0,
        }
        response = requests.post('http://listas.bitson.com.ar/mailman/subscribe/diagramacion', data=data)
        print(response)
        return Response({'mother': 'fucker'})


class DocTypeViewSet(viewsets.ModelViewSet):
    queryset = DocType.objects.all()
    serializer_class = DocTypeSerializer
