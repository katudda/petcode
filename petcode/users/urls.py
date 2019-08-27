from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet
from django.contrib.auth import views

router = routers.DefaultRouter()

router.register(r'', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('password_reset/', views.PasswordResetView.as_view(success_url=reverse_lazy('users:password_reset_done')), name='password_reset'),
]