from django.http import HttpRequest, HttpResponseNotFound
from django.shortcuts import render

from .. import forms, models


def get_news(req: HttpRequest, id: int):
    try:
        post = models.NewsPost.objects.get(id=id)
    except models.NewsPost.DoesNotExist:
        return HttpResponseNotFound

    return render(
        req,
        "newspost.html",
        {
            "form": forms.CommentForm,
            "post": post,
            "comments": post.comments.all().order_by("-created_at"),  # type: ignore
            "user": req.user,
        },
    )
