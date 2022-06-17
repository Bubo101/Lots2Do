from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from projects.models import Project

# Create your views here.
class ProjectListView(ListView):
    model = Project
    template_name = "projects/list.html"
    context_object_name = "projects_list"
