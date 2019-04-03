from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView
from dev.models import Dev
from django.urls import reverse_lazy

class DevCreateView(CreateView):
    model = Dev
    template_name = "dev/dev_create.html"
    fields = '__all__'


    def get_success_url(self):
        return reverse_lazy('post-add', kwargs={'pk': self.object.pk})

