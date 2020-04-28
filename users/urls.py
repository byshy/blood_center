from django.urls import path

from users.views import *

urlpatterns = [
    path('signup/', CreateUserViewSet.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('search/', searchView, name='search'),
    path('search/get_doners', searchView, name='search'),
]