# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Student

# Create your views here.


def index(request):
    latest_students = Student.objects.order_by('-created_on')[:5]
    template = loader.get_template('studentlist/index.html')
    context = {
        'latest_students': latest_students,
    }
    return HttpResponse(template.render(context, request))
