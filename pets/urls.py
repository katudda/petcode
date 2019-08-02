from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.list_pet),
    path('new/', views.new_pet, name='create_pet'),
    path('update_pet/<int:pk>/', views.update_pet, name='update_pet'),
    path('delete_pet/<int:pk>/', views.delete_pet, name='delete_pet'),
    path('pets/', views.home),
    path('gallery/', include('gallery.urls')),
]