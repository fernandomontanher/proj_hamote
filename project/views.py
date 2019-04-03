from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView
from project.models import Project, Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class ProjectListView(LoginRequiredMixin, ListView):

    model = Project
    template_name = "project/project_list.html"
    paginate_by = 100


    def get_context_data(self, **kwargs):
#        Project.objects.post_total()
        context = super().get_context_data(**kwargs)
        return context


class ProjectDetailView(LoginRequiredMixin, DetailView):

    model = Project
    template_name = "project/project_detail.html"

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(project_id=self.object)
        return context


class ProjectCreate(LoginRequiredMixin, CreateView):
    model = Project
    template_name = "project/project_create.html"
    fields = '__all__'

    def get_initial(self):
        return {"project": self.kwargs.get("pk")}

    def get_success_url(self):
        return reverse_lazy('post-add', kwargs={'pk': self.object.pk})


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "project/post_create.html"
    success_url = '/project/post_create/'
    fields = ['skill']

    def form_valid(self, form):
        project = Project.objects.get(id=self.kwargs.get("pk"))
        form.instance.project = project
        return super(PostCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PostCreate, self).get_context_data(**kwargs)
        context['posts'] = self.model.objects.filter(project=self.kwargs.get('pk'))
        return context

    def get_success_url(self):
        return reverse_lazy('post-add', kwargs={'pk': self.kwargs.get("pk")})

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "project/post_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy('post-add', kwargs={'pk': self.object.project_id})









