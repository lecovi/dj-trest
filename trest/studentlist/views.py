from django.shortcuts import render
from .models import Student

# Create your views here.


def index(request):
    latest_students = Student.objects.order_by('-created_on')[:5]
    context = {
        'latest_students': latest_students,
    }
    return render(request, 'studentlist/index.html', context)
