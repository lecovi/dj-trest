from django.shortcuts import render


def index(request):
    context = {
        'message': 'Student List from template!'
    }
    return render(request, 'trest/index.html', context)
