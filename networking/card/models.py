from django.db import models
from django.contrib.auth.models import User
import uuid


class BusinessCard(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} @{self.company_name} (ID: {self.id})"
