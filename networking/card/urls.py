from django.urls import path
from . import views


app_name = "card"

urlpatterns = [
    path("", views.cards_list, name="list"),
    path("<uuid:identifier>/", views.card_page, name="page_by_id"),
    path("<slug:identifier>/", views.card_page, name="page_by_slug"),
    path("new", views.card_new, name="new"),
]
