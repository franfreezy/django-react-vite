

from django.urls import path
from .views import frontpage,create_user


urlpatterns = [
    path('', frontpage, name="homepage"),
    path('register/', create_user, name="regpage"),
    
]
