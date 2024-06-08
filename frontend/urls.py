

from django.urls import path
from .views import frontpage,create_post


urlpatterns = [
    path('', frontpage, name="homepage"),
    path('register/', create_post, name="regpage"),
    
]
