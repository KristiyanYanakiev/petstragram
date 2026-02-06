from django.shortcuts import render, get_object_or_404

from pets.models import Pet


# Create your views here.
def pet_details(request, username, pet_slug):
    pet = get_object_or_404(Pet, slug=pet_slug )
    return render(request, 'pets/pet-details-page.html', {'pet': pet})

def pet_edit(request, username, pet_slug):
    render(request, 'pets/pet-edit-page.html')

def pet_delete(request, username, pet_slug):
    render(request, 'pets/pet-delete-page.html')

def add_pet(request):
    return render(request, 'pets/pet-add-page.html')