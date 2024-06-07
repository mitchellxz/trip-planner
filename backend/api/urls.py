from django.urls import path
from . import views

urlpatterns = [
    path("notes/", views.NoteListCreate.as_view(), name="note-list"),
    path("notes/delete/<int:pk>/", views.NoteDelete.as_view(), name="delete-note"),
    path("countries/", views.CountryListView.as_view(), name="country-list"),
    path('cities/', views.CityListView.as_view(), name='city-list'),


]