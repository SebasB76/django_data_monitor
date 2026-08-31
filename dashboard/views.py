from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
import requests
from django.conf import settings


@login_required
@permission_required('dashboard.index_viewer', raise_exception=True)
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