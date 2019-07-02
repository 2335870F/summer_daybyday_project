from django.apps import AppConfig
from django import forms
import entries.models
from django.contrib.auth.models import User


class EntriesConfig(AppConfig):
    name = 'entries'
