from django.conf.urls import url
from .views import index_view,add_user

urlpatterns = [
    url(r'^$', index_view, name= "index_view"),
    url(r'^add_user/$', add_user, name='add_user'),
    ]
