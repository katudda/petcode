from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.list_pet),
    path('new/', views.new_pet, name='create_pet'),
    path('pets/', views.home),
    path('gallery/', include('gallery.urls')),
]