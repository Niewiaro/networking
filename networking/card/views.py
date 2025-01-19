from django.shortcuts import render
from .models import BusinessCard
from django.contrib.auth.decorators import login_required


@login_required(login_url="/users/login/")
def cards_list(request):
    cards = BusinessCard.objects.all()
    return render(request, "card/cards_list.html", {"cards": cards})


@login_required(login_url="/users/login/")
def card_new(request):
    return render(request, "card/card_new.html")
