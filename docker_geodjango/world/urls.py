from .views import WorldViewSet
from rest_framework.routers import DefaultRouter

app_name = 'world'
router = DefaultRouter()

router.register(
    prefix="", viewset=WorldViewSet, basename="world",

)

urlpatterns = router.urls