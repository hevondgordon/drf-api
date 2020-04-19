import os

from django.conf import settings
from django.http import HttpResponse


def index(request):
    """serves documentation index"""
    return HttpResponse(os.path.join(settings.BASE_DIR, 'docs/html/index.html'))
