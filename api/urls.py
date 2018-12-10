from django.conf.urls import url, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView, UserManager

urlpatterns = {
    url(r'^bucketlists/(?P<pk>[0-9]+)/*', DetailsView.as_view(), name="details"),
    url(r'^bucketlists/*', CreateView.as_view(), name="create"),
    url(r'^auth/', include('rest_framework.urls',namespace='rest_framework')),
    url(r'^get-token/', obtain_auth_token),
    url(r'^users/*', UserManager.as_view(), name='create_user')
}

urlpatterns = format_suffix_patterns(urlpatterns)