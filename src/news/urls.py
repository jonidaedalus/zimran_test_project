from rest_framework.routers import DefaultRouter

from .views import NewsViewSet

router = DefaultRouter()

router.register(
    prefix="news",
    basename="news",
    viewset=NewsViewSet,
)

urlpatterns = router.urls
