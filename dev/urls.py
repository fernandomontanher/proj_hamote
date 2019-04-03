from django.contrib import admin
from django.urls import path
from .views import DevCreateView

urlpatterns = [
    path('signup/', DevCreateView.as_view(), name='dev-add'),

]