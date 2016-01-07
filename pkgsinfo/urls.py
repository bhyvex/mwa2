from django.conf.urls import url
import pkgsinfo.views

urlpatterns = [
    url(r'^$', pkgsinfo.views.index),
    url(r'^_list$', pkgsinfo.views.list),
    url(r'^__get_process_status$', pkgsinfo.views.status),
    url(r'^json$', pkgsinfo.views.getjson),
    url(r'^(?P<pkginfo_path>^.*$)', pkgsinfo.views.detail)
]