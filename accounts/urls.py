from django.urls import path

from accounts.views import register

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('profile/<int:pk>/', include([
        path('', show_profile_details, name='profile_details'),
        path('edit/', edit_profile, name='profile-edit'),
        path('delete/', delete_profile, name='profile-delete')
    ]))

]