from django.conf.urls import url

from cas_consumer.views import login, logout

urlpatterns[
    url(r'^login/', login, name="cas_login"),
    url(r'^logout/', logout, name="cas_logout"),
]