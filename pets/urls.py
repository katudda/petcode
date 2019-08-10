from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.list_pet),
    path('new/', views.new_pet),
    path('pet-type/new/', views.new_pet_type),
    path('update-pet/<int:pk>/', views.update_pet),
    path('<int:pk>/image/upload', views.upload_pet_image),
    path('delete-pet/<int:pk>/', views.delete_pet),
    path('delete-pet-image/<int:pk>/', views.delete_pet_image),
    path('pets/', views.home),
    path('sizes/', views.size),
    path('genders/', views.gender),
    path('categories/', views.category),
    # path('gallery/', include('gallery.urls')),
]