from django.urls import path
from api.views import (
    getNotes,
    getNote,
    updateNote,
    deletetNote,
    createNote,
)


urlpatterns = [
    path('notes/', getNotes, name="notes"),
    path('notes/create/', createNote, name="create"),
    path('notes/<str:pk>/', getNote, name="note"),
    path('notes/<str:pk>/update/', updateNote, name="update"),
    path('notes/<str:pk>/delete/', deletetNote, name="delete"),
]