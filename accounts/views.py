from django.shortcuts import render
from .admin import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('project-list')
    template_name = 'accounts/signup.html'
