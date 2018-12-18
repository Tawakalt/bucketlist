from django.conf.urls import url, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateBucketlist, BucketListDetails, UserManager, CreateCategory, CategoryDetails

urlpatterns = {
    url(r'^bucketlists/(?P<pk>[0-9]+)/*', BucketListDetails.as_view(), name="bucketlist_details"),
    url(r'^bucketlists/*', CreateBucketlist.as_view(), name="create_bucketlist"),
    url(r'^auth/', include('rest_framework.urls',namespace='rest_framework')),
    url(r'^get-token/', obtain_auth_token),
    url(r'^users/*', UserManager.as_view(), name='create_user'),
    url(r'^category/*', CreateCategory.as_view(), name="add_category"),
    url(r'^category/(?P<pk>[0-9]+)/*', CategoryDetails.as_view(), name="category_details"),
    url(r'^jwt/', obtain_jwt_token),
    url(r'^verify/', verify_jwt_token),
    url(r'^refresh/', refresh_jwt_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)