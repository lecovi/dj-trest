from django.http import Http404
from django.shortcuts import render
from .models import Student

# Create your views here.


def index(request):
    latest_students = Student.objects.order_by('-created_on')[:5]
    context = {
        'latest_students': latest_students,
    }
    return render(request, 'studentlist/index.html', context)


def details(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        raise Http404('Student does not exist')
    context = {
        'student': student
    }
    return render(request, 'studentlist/details.html', context)
