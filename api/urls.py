from django.urls import path, include

from api.views import BloodCenterListView, BloodCenterView, DonorView

urlpatterns = [
    path('blood_centers/', BloodCenterListView.as_view(), name='get_blood_centers'),
    path('blood_center/<str:name>', BloodCenterView.as_view(), name='get_blood_center'),
    path('donor/<int:id>', DonorView.as_view(), name='get_donor'),
    path('auth/', include('rest_auth.urls')),   # DRF auth system
]
