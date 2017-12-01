from django.conf.urls import url
from rest_framework import routers
from .views import ContactsViewSetSet


router = routers.DefaultRouter()
router.register(r'contacts', ContactsViewSetSet, base_name='contacts')

urlpatterns = router.urls