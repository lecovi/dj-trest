import requests
from django.shortcuts import render, get_object_or_404
from .models import Student, DocType
from rest_framework import viewsets
from rest_framework.decorators import action
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

    def create(self, request, *args, **kwargs):
        print('extra function')
        data = {
            'email': request.POST['email'],
            'fullname': '{} {}'.format(request.POST['name'], request.POST['lastname']),
            'pw': request.POST['doc_number'],
            'pw-conf': request.POST['doc_number'],
            'digest': 0,
        }
        response = requests.post('http://listas.bitson.com.ar/mailman/subscribe/diagramacion', data=data)
        print(response)
        return super().create(request)


class DocTypeViewSet(viewsets.ModelViewSet):
    queryset = DocType.objects.all()
    serializer_class = DocTypeSerializer
