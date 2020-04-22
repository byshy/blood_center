from django.urls import path, include

from api.views import BloodCenterListView, BloodCenterView

urlpatterns = [
    path('blood_centers/', BloodCenterListView.as_view(), name='get_blood_centers'),
    path('blood_center/<str:id>', BloodCenterView.as_view(), name='get_blood_center'),
    path('auth/', include('rest_auth.urls')),   # DRF auth system
]
