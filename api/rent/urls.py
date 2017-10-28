from .views import rent_item
from django.conf.urls import url

urlpatterns = [
    url(r'^items/', rent_item),
]
