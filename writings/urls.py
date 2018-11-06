from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url
from django.contrib import admin
from writings.views import writing_detailview, writing_listview, writing_createview, WritingEdit 


urlpatterns = [
    url(r'^$', writing_listview,name="list"),
    url(r'^create$', writing_createview,name="create"),
	url(r'^(?P<pk>\w+)$', writing_detailview,name="detail"),
    url(r'^edit/(?P<pk>\w+)$', WritingEdit.as_view(),name="update"),
]
