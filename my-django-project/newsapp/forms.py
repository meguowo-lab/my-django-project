from django.contrib.auth.forms import AuthenticationForm
from django.forms import BooleanField, CharField, Form, PasswordInput


class CommentForm(Form):
    body = CharField(max_length=1000, min_length=1)


class LoginForm(AuthenticationForm):
    username = CharField()
    password = CharField(widget=PasswordInput())
    remember_me = BooleanField(initial=False, required=False)
