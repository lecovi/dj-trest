from django.shortcuts import render, get_object_or_404
from .models import Student, DocType
from rest_framework import viewsets
from .serializers import StudentSerializer, DocTypeSerializer
# Create your views here.


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


class DocTypeViewSet(viewsets.ModelViewSet):
    queryset = DocType.objects.all()
    serializer_class = DocTypeSerializer
