from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.list_pet),
    path('new/', views.new_pet),
    path('update-pet/<int:pk>/', views.update_pet),
    path('<int:pk>/image/upload', views.upload_pet_image),
    path('delete_pet/<int:pk>/', views.delete_pet),
    path('pets/', views.home),
    path('sizes/', views.size),
    path('genders/', views.gender),
    path('categories/', views.category),
    # path('gallery/', include('gallery.urls')),
]