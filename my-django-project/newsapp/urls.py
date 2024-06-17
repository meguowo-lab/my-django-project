from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

urlpatterns = [  # type: ignore
    path("", views.home, name="home"),
    path("comments/create/<int:post_id>", views.add_comment, name="comments_create"),
    path(
        "accounts/login/",
        views.MyLoginView.as_view(
            template_name="login.html", redirect_authenticated_user=True
        ),
        name="login",
    ),
    path("accounts/logout/", LogoutView.as_view(), name="logout"),
    path("accounts/register", views.RegisterView.as_view(), name="register"),
    path("news/<int:id>", views.get_news, name="news_get"),  # type: ignore
]
