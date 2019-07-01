from django.apps import AppConfig
from django import forms
import recipes.models
from django.contrib.auth.models import User


class RecipesConfig(AppConfig):
    name = 'recipes'
