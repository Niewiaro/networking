from django.shortcuts import render
from .models import BusinessCard


def cards_list(request):
    cards = BusinessCard.objects.all()
    return render(request, "card/cards_list.html", {"cards": cards})
