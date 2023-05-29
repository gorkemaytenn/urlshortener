from rest_framework.routers import DefaultRouter

from urlshortener.shorturls.views import URLShortenerViewset

router = DefaultRouter()


router.register(r"shorturls", URLShortenerViewset, basename="shorturls")

app_name = 'shorturls'

urlpatterns = router.urls
