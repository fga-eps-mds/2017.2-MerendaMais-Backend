from django.conf.urls import url, include
from rest_framework import routers
from backend.views import (
    CustomObtainAuthToken, CounselorViewSet, SchoolViewSet
)

router = routers.DefaultRouter()
router.register(r'counselor', CounselorViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(
        r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
    url(
        r'^get_auth_token/$',
        CustomObtainAuthToken.as_view(),
        name='get_auth_token'
    ),
    url(
        r'^get_schools/$',
        SchoolViewSet.as_view({'post': 'get_schools'}),
        name='get_schools'
    )
]
