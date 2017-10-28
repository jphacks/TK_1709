# from rest_framework import routers
from .views import return_item
from django.conf.urls import url

# router = routers.DefaultRouter()
# router.register(r'items', validate_image)

urlpatterns = [
    url(r'^items/', return_item),
]
