from django.conf.urls import (
    url,
    include
)
from server.web.views.errors import (
    handle_400,
    handle_403,
    handle_404,
    handle_500
)
from server.web.views.index import index


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^400.html$', handle_400),
    url(r'^403.html$', handle_403),
    url(r'^404.html$', handle_404),
    url(r'^500.html$', handle_500),
]

handler400 = 'server.web.views.errors.handle_400'
handler403 = 'server.web.views.errors.handle_403'
handler404 = 'server.web.views.errors.handle_404'
handler500 = 'server.web.views.errors.handle_500'
