from django.views.generic import ListView ,CreateView , UpdateView , DeleteView
from django.urls import reverse_lazy , reverse
from .import models
from .import forms
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class ProjectListView(LoginRequiredMixin, ListView):
    model = models.Project
    template_name = 'project/list.html'
    paginate_by = 2
    def get_queryset(self):
        query_set = super().get_queryset()
        where = {}
        q = self.request.GET.get('q' , None)
        if q: 
            where['title__icontains'] = q
        return query_set.filter(**where)
    

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = models.Project
    form_class = forms.ProjectCreateForm
    template_name = 'project/create.html'
    success_url = reverse_lazy('Project_list')



class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Project
    form_class = forms.ProjectUpdateForm
    template_name = 'project/update.html'
    success_url = reverse_lazy('Project_list')

    def get_success_url(self):
        return reverse ('Project_update', args=[self.object.id] )

class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Project
   # fields = ['is_completed']
    
    template_name = 'project/delete.html'
    success_url = reverse_lazy('Project_list')



    def get_success_url(self):
        return reverse ('Project_update', args=[self.object.id] )
    

    
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = models.Task
    fields = ['project', 'description']
    http_method_names = ['post']


    def get_success_url(self):
        return reverse ('Project_update', args=[self.object.project.id] )
    

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Task
    fields = ['is_completed']
    http_method_names = ['post']


    def get_success_url(self):
        return reverse ('Project_update', args=[self.object.project.id] )
    
class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Task

    def get_success_url(self):
        return reverse ('Project_update', args=[self.object.project.id] )
    