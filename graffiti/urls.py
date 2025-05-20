from django.urls import path

from . import views

app_name = "graffiti"

urlpatterns = [
    path("create/", views.graffiti_create, name="create"),
    path("<int:pk>/", views.graffiti_detail, name="detail"),
    path("<int:pk>/delete/", views.graffiti_delete, name="delete"),
    path("like/<int:pk>/", views.like_graffiti, name="like"),
]
