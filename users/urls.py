from django.urls import path
from .views import login, registration, profile

app_name = 'users'

urlpatterns = [
    path('login/', login, name = 'login'), # ...users/login (users берется из главного файла urls.py
                                            # в проекте (из store))
    path('registration/', registration, name = 'registration'),
    path('profile/', profile, name = 'profile')
]