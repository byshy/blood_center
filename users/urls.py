from django.urls import path

from users.views import CreateUserViewSet, CustomLoginView

urlpatterns = [
    path('signup/', CreateUserViewSet.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
]