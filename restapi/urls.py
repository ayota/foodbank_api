from django.conf.urls import url, include
from rest_framework import routers
from restapi import views

router = routers.DefaultRouter(schema_title='CAFB Food Scanner API')
router.register(r'api/v1/scan', views.ScanViewSet)
router.register(r'api/v1/foodcat', views.FoodCatViewSet)
router.register(r'api/v1/wellscore', views.WellScoreViewSet)
router.register(r'api/v1/nutrule', views.NutRuleViewSet)
router.register(r'api/v1/upc', views.UPCViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api/v1/', include('rest_framework.urls', namespace='rest_framework')),
        url(r'^scan/(?P<upc>[0-9]+)/$', views.scan_view),
]