from django.shortcuts import render, get_object_or_404

from photos.models import Photo


# Create your views here.
def add_photo_page(request):
    return render(request, 'photos/photo-add-page.html')

def photo_details(request, pk):
    photo = get_object_or_404(Photo, pk=pk)

    return render(request, 'photos/photo-details-page.html', {'photo': photo})


def photo_edit(request, pk):
    return render(request, 'photos/photo-edit-page.html')