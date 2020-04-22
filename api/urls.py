from django.urls import path, include

from api.views import BloodCenterListView

urlpatterns = [
    path('blood_centers/', BloodCenterListView.as_view(), name='get_blood_centers'),
    path('auth/', include('rest_auth.urls')),   # DRF auth system
]
