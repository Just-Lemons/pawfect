from django.urls import path,include
from . import views

urlpatterns = [
    path('<int:pet_id>/', views.details,name='details'),
    
]