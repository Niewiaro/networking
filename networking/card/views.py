from django.shortcuts import render, get_object_or_404
from .models import BusinessCard
from django.contrib.auth.decorators import login_required
import uuid


@login_required(login_url="/users/login/")
def cards_list(request):
    cards = BusinessCard.objects.all()
    return render(request, "card/cards_list.html", {"cards": cards})


@login_required(login_url="/users/login/")
def card_new(request):
    return render(request, "card/card_new.html")


@login_required(login_url="/users/login/")
def card_page(request, identifier):
    if isinstance(identifier, uuid.UUID):  # Sprawdzenie czy to UUID
        card = get_object_or_404(BusinessCard, id=identifier)
    else:  # W przeciwnym razie traktujemy jako slug
        card = get_object_or_404(BusinessCard, slug=identifier)

    return render(request, "card/card_page.html", {"card": card})
