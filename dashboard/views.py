from django.shortcuts import render

import requests
from django.conf import settings


def index(request):
    try:
        response = requests.get(settings.API_URL, timeout=10)
        posts = response.json() or {}
    except requests.RequestException:
        posts = {}

    data = {
        'title': "Landing Page' Dashboard",
        'total_responses': len(posts),
    }

    return render(request, 'dashboard/index.html', data)