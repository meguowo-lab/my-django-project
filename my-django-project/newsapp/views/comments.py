from django.contrib.auth.decorators import login_required
from django.http import (
    HttpRequest,
    HttpResponseBadRequest,
    HttpResponseNotFound,
)
from django.shortcuts import redirect
from django.views.decorators.http import require_POST

from .. import forms, models


@require_POST
@login_required(redirect_field_name="")
def add_comment(req: HttpRequest, post_id: int):
    form = forms.CommentForm(req.POST)

    if not form.is_valid():
        return HttpResponseBadRequest()

    try:
        post = models.NewsPost.objects.get(id=post_id)
    except models.NewsPost.DoesNotExist:
        return HttpResponseNotFound()

    comment = models.Comment(body=form.cleaned_data["body"], author=req.user, post=post)

    comment.save()

    return redirect("news_get", post_id)
