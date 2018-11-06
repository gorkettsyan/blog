from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns




urlpatterns = [

    url(r'^admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
	url(r'^', include("home.urls", namespace="home")),
    url(r'^writings/', include("writings.urls", namespace="writings")),
    url(r'^accounts/', include("accounts.urls", namespace="accounts")),
    prefix_default_language = False,
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
