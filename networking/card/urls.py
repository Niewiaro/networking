from django.urls import path
from . import views


app_name = "card"

urlpatterns = [
    path("", views.cards_list, name="list"),
]
