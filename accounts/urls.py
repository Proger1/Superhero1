from django.urls import path
from . import views



urlpatterns = [
    path('',views.home, name="home"),
    path('superheroes/',views.superheroes, name="superheroes"),
    path( 'create_superhero/', views.createSuperhero, name="create_superhero"),
    path( 'edit_superhero/<str:pk>', views.editSuperhero, name="edit_superhero"),
    path( 'delete_superhero/<str:pk>', views.deleteSuperhero, name="delete_superhero"),
    
]

