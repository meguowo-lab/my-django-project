from .comments import add_comment
from .home import home
from .login import MyLoginView
from .news import get_news
from .register import RegisterView

__all__ = ["add_comment", "home", "MyLoginView", "get_news", "RegisterView"]
