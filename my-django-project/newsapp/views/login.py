from django.contrib.auth.views import LoginView
from django.http import HttpResponse

from .. import forms


class MyLoginView(LoginView):
    form_class = forms.LoginForm

    def form_valid(self, form: forms.AuthenticationForm) -> HttpResponse:
        if not form.cleaned_data["remember_me"]:
            self.request.session.set_expiry(0)

        return super().form_valid(form)
