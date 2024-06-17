from django.http import HttpRequest
from django.shortcuts import render

from .. import models


def home(request: HttpRequest):
    return render(
        request,
        "home.html",
        {"news": models.NewsPost.objects.all().order_by("-created_at")},
    )
