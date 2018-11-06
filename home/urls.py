from django.conf.urls import url
from home.views import homeview, aboutview, contactview
from django.conf import settings
from home.views import homeview, aboutview, contactview, homeview



urlpatterns = [

    url(r'^$', homeview, name="homepage"),
    url(r'^about/$', aboutview,name="about"),
	url(r'^contact/$', contactview,name="contact"),

]
