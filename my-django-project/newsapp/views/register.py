from typing import Any

from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View


class RegisterView(View):
    form_class = UserCreationForm
    template_name = "register.html"

    def dispatch(self, req: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if req.user.is_authenticated:
            return redirect("home")

        return super().dispatch(req, *args, **kwargs)

    def get(self, req: HttpRequest, *args: Any, **kwargs: Any):
        return render(req, self.template_name, {"form": self.form_class})

    def post(self, req: HttpRequest, *args: Any, **kwargs: Any):
        form = self.form_class(req.POST)

        if not form.is_valid():
            return render(req, self.template_name, {"form": form})

        form.save(commit=True)

        return redirect("login")
