from django.conf.urls import url
from .views import game_detail, make_move_view, AllGamesList

urlpatterns = [
    url(r'detail/(?P<id>\d+)/$', game_detail, name = 'gameplay_detail'),
    url(r'makemove/(?P<id>\d+)/$', make_move_view, name = 'make_move_url'),
    url(r'all$', AllGamesList.as_view())


]