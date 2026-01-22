from django.urls import path, include

from pets.views import pet_details, pet_edit, pet_delete, add_pet

urlpatterns = [
    path('add/', add_pet, name='add-pet'),

    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', pet_details, name='pet-details'),
        path('edit/', pet_edit, name='pet-edit'),
        path('delete/', pet_delete, name='pet-delete')
    ]))
]


