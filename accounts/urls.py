from django.conf.urls import url
from django.contrib.auth.views import logout
from django.views.decorators.csrf import csrf_exempt
from writers.settings import LOGOUT_REDIRECT_URL
from django.contrib.auth.views import LoginView
from .views import( user_registerview,profile_listview ,activate ,profile_detailview,
profile_detail_writings,ProfileEdit )


urlpatterns = [

	url(r'^register/$', csrf_exempt(user_registerview),name="register"),
	url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    csrf_exempt(activate), name='activate'),
   	url(r'^profiles/$', profile_listview,name="profiles"),
	url(r'^profiles/edit/(?P<pk>\w+)/$', ProfileEdit.as_view(),name="profile-edit"),
   	url(r'^profiles/(?P<pk>\w+)/writings/$', profile_detail_writings,name="profile_detail"),
   	url(r'^profiles/(?P<user_id>\w+)/$', profile_detailview,name="profile-detail"),
    url(r'^login/$', LoginView.as_view(template_name='accounts/login.html', redirect_authenticated_user=True),name="login"),
    url(r'^logout/$', logout, {'next_page': LOGOUT_REDIRECT_URL}, name='logout')
]
