from django.contrib import admin
from django.urls import path
from .views import ProjectListView, ProjectDetailView, ProjectCreate, PostCreate, PostDelete

urlpatterns = [
    path('post_delete/<int:pk>/', PostDelete.as_view(), name='post-delete'),
    path('busca/', ProjectListView.as_view(), name='project-list'),
    path('project_detail/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('project_create/', ProjectCreate.as_view(), name='project-add'),
    path('post_create/<int:pk>/', PostCreate.as_view(), name='post-add'),
]
