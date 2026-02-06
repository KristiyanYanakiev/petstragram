from django.urls import path

from photos.views import add_photo_page, photo_details, photo_edit

app_name = 'photos'
urlpatterns = [
    path('add/', add_photo_page, name='add-photo'),
    path('<int:pk>/', photo_details, name='photo-details' ),
    path('<int:pk>/edit/', photo_edit, name='photo-edit')


]



