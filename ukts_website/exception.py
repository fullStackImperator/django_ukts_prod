# yourproject/exception.py
from django.shortcuts import render


def handler404(request, *args, **argv):
    response = render(request, 'ukts/404.html')
    response.status_code = 404
    return response