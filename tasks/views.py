from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from tasks.models import Task
from django.urls import reverse_lazy

# Create your views here.


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/newtask.html"
    fields = ["name", "start_date", "due_date", "project", "assignee"]

    def get_success_url(self):
        return reverse_lazy(
            "show_project", kwargs={"pk": self.object.project.pk}
        )


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/tasklist.html"
    context_object_name = "task_list"

    def get_queryset(self):
        return Task.objects.filter(assignee=self.request.user)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ["is_completed"]
    success_url = reverse_lazy("show_my_tasks")
