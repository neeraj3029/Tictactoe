from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

from .views import home, new_invitation, accept_invitation, invi, SignUpView

urlpatterns = [
    url(r'home$', home, name="player_home"),
    url(r'login$',
        LoginView.as_view(template_name="players/login_form.html"),
        name="login_page"),
    url(r'logout$',
        LogoutView.as_view(),
        name="logout_page"),
    url(r'new_invitation$', new_invitation, name="player_new_invitation"),
    url(r'accept_invitation/(?P<id>\d+)/$',
        accept_invitation,
        name="player_accept_invitation"),
    url(r'all$', invi.as_view()),
    url(r'signup$', SignUpView.as_view(), name='player_signup')
]